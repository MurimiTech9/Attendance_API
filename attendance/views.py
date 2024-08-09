from rest_framework import viewsets
from .models import AttendanceRecord, LeaveRequest, Holiday
from .serializers import AttendanceRecordSerializer, LeaveRequestSerializer, HolidaySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'date', 'status']
    search_fields = ['employee__name', 'status']
    ordering_fields = ['date', 'employee__name']

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'start_date', 'leave_type', 'status']
    search_fields = ['employee__name', 'leave_type']
    ordering_fields = ['start_date', 'employee__name']

class HolidayViewSet(viewsets.ModelViewSet):
    queryset = Holiday.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['date']
    search_fields = ['name']
    ordering_fields = ['date', 'name']


