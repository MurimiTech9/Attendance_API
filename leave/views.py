from django.shortcuts import render
from rest_framework import viewsets
from .models import LeaveRequest
from .serializers import LeaveRequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['employee', 'start_date', 'leave_type', 'status']
    search_fields = ['employee__name', 'leave_type']
    ordering_fields = ['start_date', 'employee__name']

def leave_request(request):
    return render(request, 'leave/leave_request.html')