from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom filters
class RoleFilter(admin.SimpleListFilter):
    title = 'User Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            ('REPORTER', 'Reporters'),
            ('COLLECTOR', 'Collectors'),
            ('ADMIN', 'Admins'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(role=self.value())
        return queryset


class StatusFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('PENDING', 'Pending Approval'),
            ('APPROVED', 'Approved'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset


# Base User Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'status', 'points', 'date_joined', 'is_active']
    list_filter = [RoleFilter, StatusFilter, 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'status', 'points')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Fields', {'fields': ('role', 'status', 'points')}),
    )
    
    actions = ['approve_users', 'mark_as_pending', 'reset_points']
    
    def approve_users(self, request, queryset):
        updated = queryset.update(status='APPROVED')
        self.message_user(request, f'{updated} user(s) approved successfully.')
    approve_users.short_description = "Approve selected users"
    
    def mark_as_pending(self, request, queryset):
        updated = queryset.update(status='PENDING')
        self.message_user(request, f'{updated} user(s) marked as pending.')
    mark_as_pending.short_description = "Mark as pending"
    
    def reset_points(self, request, queryset):
        updated = queryset.update(points=0)
        self.message_user(request, f'Points reset for {updated} user(s).')
    reset_points.short_description = "Reset points to 0"


# Reporter Admin
class ReporterAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role='REPORTER')
    
    def has_add_permission(self, request):
        return True
    
    def save_model(self, request, obj, form, change):
        obj.role = 'REPORTER'
        super().save_model(request, obj, form, change)


# Collector Admin
class CollectorAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role='COLLECTOR')
    
    def has_add_permission(self, request):
        return True
    
    def save_model(self, request, obj, form, change):
        obj.role = 'COLLECTOR'
        super().save_model(request, obj, form, change)


# Admin User Admin
class AdminUserAdmin(CustomUserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(role='ADMIN')
    
    def has_add_permission(self, request):
        return True
    
    def save_model(self, request, obj, form, change):
        obj.role = 'ADMIN'
        obj.is_staff = True
        super().save_model(request, obj, form, change)


# Proxy models for separate admin sections
class Reporter(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Reporter'
        verbose_name_plural = 'Reporters'


class Collector(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Collector'
        verbose_name_plural = 'Collectors'


class AdminUser(CustomUser):
    class Meta:
        proxy = True
        verbose_name = 'Admin User'
        verbose_name_plural = 'Admin Users'


# Register models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Collector, CollectorAdmin)
admin.site.register(AdminUser, AdminUserAdmin)

# Customize admin site headers
admin.site.site_header = "EcoWaste Administration"
admin.site.site_title = "EcoWaste Admin"
admin.site.index_title = "Welcome to EcoWaste Administration Panel"
