from django.db import models
from employees.models import Employee
from datetime import datetime, timedelta
from django.contrib import admin

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    check_in_time = models.TimeField()
    check_out_time = models.TimeField(null=True, blank=True)
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
        ('Half-day', 'Half-day'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    SHIFT_CHOICES = [
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    ]
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES, default='Day')
# Auto calculate total_work_hours
    @admin.display(description='Total Work Hours')
    def calculate_work_hours(self):
        if self.check_in_time and self.check_out_time:
            # Create a dummy date to combine with the time
            dummy_date = datetime.now().date()
            
            # Combine the dummy date with check_in and check_out times
            check_in_datetime = datetime.combine(dummy_date, self.check_in_time)
            check_out_datetime = datetime.combine(dummy_date, self.check_out_time)
            
            # If check_out is earlier than check_in, assume it's the next day
            if check_out_datetime < check_in_datetime:
                check_out_datetime += timedelta(days=1)
            
            # Calculate the time difference
            time_difference = check_out_datetime - check_in_datetime
            
            # Convert the time difference to hours
            hours_worked = time_difference.total_seconds() / 3600
            
            return round(hours_worked, 2)  # Round to 2 decimal places
        return 0  # Return 0 if check_in_time or check_out_time is not set    return 0

def save(self, *args, **kwargs):
    self.total_work_hours = self.calculate_work_hours()
    super().save(*args, **kwargs)

def __str__(self):
    return f"{self.employee} - {self.date} - {self.status} - {self.shift}"
  
class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    LEAVE_TYPES = [
        ('Sick', 'Sick'),
        ('Vacation', 'Vacation'),
        ('Personal', 'Personal'),
    ]
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPES)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField()

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date})"

class Holiday(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}"
    

