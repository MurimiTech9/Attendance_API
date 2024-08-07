from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceRecordViewSet, LeaveRequestViewSet, HolidayViewSet

router = DefaultRouter()
router.register(r'attendance', AttendanceRecordViewSet)
router.register(r'leave-requests', LeaveRequestViewSet)
router.register(r'holidays', HolidayViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
