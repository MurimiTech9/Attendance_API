from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceRecordViewSet, HolidayViewSet, AttendanceRecordListViewSet
from . import views

router = DefaultRouter()
router.register(r'attendance', AttendanceRecordViewSet, basename='attendance-api')
#router.register(r'leave-requests', LeaveRequestViewSet)
router.register(r'holidays', HolidayViewSet)
router.register(r'attendance-records', AttendanceRecordListViewSet, basename='attendance-web')


urlpatterns = [
    path('', include(router.urls)),
    path('attendance/', views.attendance_record_list, name='attendance_record_list'),
    path('attendance/records/', views.attendance_record_list_view, name='attendance_record_list_view'),
]
