from django.contrib import admin
from .models import AttendanceRecord, LeaveRequest, Holiday

admin.site.register(AttendanceRecord)
admin.site.register(LeaveRequest)
admin.site.register(Holiday)
