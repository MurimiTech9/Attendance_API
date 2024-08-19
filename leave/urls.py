
from django.urls import path
from leave import views 
from .views import LeaveRequestAPIView, LeaveDetailAPIView


urlpatterns = [
    path('leave/', views.leave_request, name='leave_request_list'),
    path('api/leave/', LeaveRequestAPIView.as_view(), name='leave-request-list-api'),
    path('api/leave/<uuid:pk>/', LeaveDetailAPIView.as_view(), name='leave-request-detail-api'),
]