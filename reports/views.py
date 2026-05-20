from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import WasteReport, Feedback
from .forms import WasteReportForm, FeedbackForm
from accounts.decorators import reporter_required, collector_required, admin_required

CustomUser = get_user_model()

@reporter_required
def reporter_dashboard(request):
    if request.method == 'POST':
        form = WasteReportForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                report = form.save(commit=False)
                report.reporter = request.user
                report.save()
                
                request.user.points += 10
                request.user.save()
                
                messages.success(request, 'Waste report submitted successfully. You earned 10 points!')
                return redirect('reporter_dashboard')
    else:
        form = WasteReportForm()
        
    reports = WasteReport.objects.filter(reporter=request.user).exclude(status='REJECTED').order_by('-created_at')
    return render(request, 'reports/reporter_dashboard.html', {'form': form, 'reports': reports})

@collector_required
def collector_dashboard(request):
    if request.method == 'POST':
        if 'ignore_report' in request.POST:
            report_id = request.POST.get('report_id')
            report = get_object_or_404(WasteReport, id=report_id, status='PENDING')
            report.ignored_by.add(request.user)
            messages.success(request, 'Report hidden from your feed.')
            return redirect('collector_dashboard')
            
        elif 'cancel_report' in request.POST:
            report_id = request.POST.get('report_id')
            report = get_object_or_404(WasteReport, id=report_id, collector=request.user, status='COLLECTED')
            
            with transaction.atomic():
                report.status = 'PENDING'
                report.collector = None
                report.save()
                
                # Remove feedback associated with it since it's cancelled
                if hasattr(report, 'feedback'):
                    report.feedback.delete()
                    
                messages.success(request, 'Collection cancelled successfully. The report is back in the feed.')
                return redirect('collector_dashboard')
                
        else:
            report_id = request.POST.get('report_id')
            report = get_object_or_404(WasteReport, id=report_id, status='PENDING')
            form = FeedbackForm(request.POST)
            
            if form.is_valid():
                with transaction.atomic():
                    report.status = 'COLLECTED'
                    report.collector = request.user
                    report.save()
                    
                    feedback = form.save(commit=False)
                    feedback.report = report
                    feedback.save()
                    
                    messages.success(request, 'Waste report marked as collected successfully!')
                    return redirect('collector_dashboard')
    else:
        form = FeedbackForm()
        
    pending_reports = WasteReport.objects.filter(status='PENDING').exclude(ignored_by=request.user).order_by('-created_at')
    my_collections = WasteReport.objects.filter(collector=request.user).order_by('-updated_at')
    return render(request, 'reports/collector_dashboard.html', {
        'pending_reports': pending_reports, 
        'my_collections': my_collections,
        'form': form
    })

@admin_required
def admin_dashboard(request):
    # Handle Collector Approval
    if request.method == 'POST' and 'approve_collector' in request.POST:
        user_id = request.POST.get('user_id')
        user = get_object_or_404(CustomUser, id=user_id, role='COLLECTOR', status='PENDING')
        user.status = 'APPROVED'
        user.save()
        messages.success(request, f'Collector {user.username} approved successfully.')
        return redirect('admin_dashboard')
        
    # Handle Report Verification
    if request.method == 'POST' and 'verify_report' in request.POST:
        report_id = request.POST.get('report_id')
        report = get_object_or_404(WasteReport, id=report_id, status='COLLECTED')
        
        with transaction.atomic():
            report.status = 'VERIFIED'
            report.verified_by = request.user  # Track which admin verified
            report.save()
            
            if report.collector:
                report.collector.points += 20
                report.collector.save()
                messages.success(request, f'Report verified. 20 points awarded to {report.collector.username}.')
            else:
                 messages.warning(request, 'Report verified, but no collector found to award points to.')
                 
        return redirect('admin_dashboard')

    # Handle Report Rejection
    if request.method == 'POST' and 'reject_report' in request.POST:
        report_id = request.POST.get('report_id')
        rejection_reason = request.POST.get('rejection_reason', '')
        report = get_object_or_404(WasteReport, id=report_id, status='COLLECTED')
        
        with transaction.atomic():
            report.status = 'REJECTED'
            report.rejection_reason = rejection_reason
            report.verified_by = request.user  # Track which admin rejected
            report.save()
            
            # Duplicate the report for the feed/reporter so it can be collected again
            new_report = WasteReport.objects.create(
                location=report.location,
                waste_type=report.waste_type,
                amount=report.amount,
                reporter=report.reporter,
                status='PENDING'
            )
            
            messages.success(request, 'Report collection rejected. The report has been returned to the pending feed.')
                 
        return redirect('admin_dashboard')

    # Statistics for dashboard cards
    from django.db.models import Sum, Count
    
    total_reports = WasteReport.objects.count()
    pending_collectors = CustomUser.objects.filter(role='COLLECTOR', status='PENDING')
    pending_collectors_count = pending_collectors.count()
    active_collectors = CustomUser.objects.filter(role='COLLECTOR', status='APPROVED').count()
    
    # Calculate total waste collected (sum of verified reports)
    # Since amount is CharField, we'll count verified reports instead
    total_waste_collected = WasteReport.objects.filter(status='VERIFIED').count()
    
    # Waste type distribution for chart
    waste_distribution = WasteReport.objects.values('waste_type').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Recent activity feed (last 10 activities)
    recent_reports = WasteReport.objects.select_related('reporter', 'collector').order_by('-updated_at')[:10]
    
    collected_reports = WasteReport.objects.filter(status='COLLECTED').order_by('-updated_at')
    
    # Get admin's task history (verified and rejected reports)
    admin_history = WasteReport.objects.filter(
        verified_by=request.user
    ).filter(
        status__in=['VERIFIED', 'REJECTED']
    ).order_by('-updated_at')
    
    return render(request, 'reports/admin_dashboard.html', {
        'pending_collectors': pending_collectors,
        'collected_reports': collected_reports,
        'admin_history': admin_history,
        # Statistics
        'total_reports': total_reports,
        'pending_collectors_count': pending_collectors_count,
        'active_collectors': active_collectors,
        'total_waste_collected': total_waste_collected,
        'waste_distribution': waste_distribution,
        'recent_reports': recent_reports,
    })

def leaderboard(request):
    top_reporters = CustomUser.objects.filter(role='REPORTER').order_by('-points')[:50]
    top_collectors = CustomUser.objects.filter(role='COLLECTOR').order_by('-points')[:50]
    return render(request, 'reports/leaderboard.html', {
        'top_reporters': top_reporters,
        'top_collectors': top_collectors
    })
