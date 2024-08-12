from django.contrib import admin
from .models import LeaveRequest

# Register your models here.

admin.site.register(LeaveRequest)

class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status')
    search_fields = ('employee__email',)
    readonly_fields = ('status',)