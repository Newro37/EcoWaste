from django.contrib import admin
from .models import WasteReport, Feedback

# Waste Report Admin
class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0
    readonly_fields = ['content', 'created_at']
    can_delete = False


class WasteReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'waste_type', 'location', 'amount', 'reporter', 'collector', 'status', 'created_at']
    list_filter = ['status', 'waste_type', 'created_at', 'updated_at']
    search_fields = ['location', 'reporter__username', 'collector__username', 'rejection_reason']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Report Information', {
            'fields': ('waste_type', 'location', 'amount', 'reporter')
        }),
        ('Collection Details', {
            'fields': ('collector', 'status', 'rejection_reason')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [FeedbackInline]
    
    actions = ['mark_as_verified', 'mark_as_rejected', 'mark_as_pending']
    
    def mark_as_verified(self, request, queryset):
        updated = queryset.update(status='VERIFIED')
        self.message_user(request, f'{updated} report(s) marked as verified.')
    mark_as_verified.short_description = "Mark as Verified"
    
    def mark_as_rejected(self, request, queryset):
        updated = queryset.update(status='REJECTED')
        self.message_user(request, f'{updated} report(s) marked as rejected.')
    mark_as_rejected.short_description = "Mark as Rejected"
    
    def mark_as_pending(self, request, queryset):
        updated = queryset.update(status='PENDING')
        self.message_user(request, f'{updated} report(s) marked as pending.')
    mark_as_pending.short_description = "Mark as Pending"


# Feedback Admin
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'report', 'get_reporter', 'get_collector', 'content_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'report__location', 'report__reporter__username']
    readonly_fields = ['report', 'content', 'created_at']
    ordering = ['-created_at']
    
    def get_reporter(self, obj):
        return obj.report.reporter.username if obj.report.reporter else 'N/A'
    get_reporter.short_description = 'Reporter'
    
    def get_collector(self, obj):
        return obj.report.collector.username if obj.report.collector else 'N/A'
    get_collector.short_description = 'Collector'
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Feedback'


# Register models
admin.site.register(WasteReport, WasteReportAdmin)
admin.site.register(Feedback, FeedbackAdmin)
