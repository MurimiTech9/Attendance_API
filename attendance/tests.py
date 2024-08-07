from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import AttendanceRecord
from employees.models import Employee

class AttendanceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.employee = Employee.objects.create(user=self.user)
        
    def test_attendance_record_creation(self):
        record = AttendanceRecord.objects.create(
            employee=self.employee,
            date='2023-01-01',
            check_in_time='09:00:00',
            status='Present'
        )
        self.assertTrue(isinstance(record, AttendanceRecord))
        self.assertEqual(record.__str__(), f"{self.employee} - 2023-01-01 - Present")

class AttendanceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(user=self.user)
        
    def test_attendance_list(self):
        response = self.client.get('/attendance/attendance/')
        self.assertEqual(response.status_code, 200)

    def test_create_attendance(self):
        data = {
            'employee': self.employee.id,
            'date': '2023-01-01',
            'check_in_time': '09:00:00',
            'status': 'Present'
        }
        response = self.client.post('/attendance/attendance/', data)
        self.assertEqual(response.status_code, 201)
