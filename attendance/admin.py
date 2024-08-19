from typing import Any
from django.contrib import admin
from .models import AttendanceRecord, Holiday

admin.site.register(Holiday)

@admin.register(AttendanceRecord)

class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'is_absent', 'check_in_time', 'check_out_time', 'calculate_work_hours', 'status', 'shift')
    readonly_fields = ('calculate_work_hours',)
    radio_fields = {'status': admin.VERTICAL, 'shift': admin.HORIZONTAL}

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        form.base_fields['check_in_time'].required = False
        form.base_fields['check_out_time'].required = False
        return form
    
    def save_model(self, request: Any, obj: Any, form: Any, change):
        if obj.is_absent:
            obj.check_in_time = None
            obj.check_out_time = None
        super().save_model(request, obj, form, change)

    class Media:
        js = ('attendance/js/attendance_record_admin.js',)