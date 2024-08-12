from django.contrib import admin
from .models import AttendanceRecord, LeaveRequest, Holiday

admin.site.register(LeaveRequest)
admin.site.register(Holiday)

@admin.register(AttendanceRecord)

class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'check_in_time', 'check_out_time', 'calculate_work_hours', 'status', 'shift')
    readonly_fields = ('calculate_work_hours',)