from django.db import models
from employees.models import Employee

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

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

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
