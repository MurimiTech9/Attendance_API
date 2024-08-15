
from django.urls import path
from leave import views 
from .views import LeaveRequestAPIView


urlpatterns = [
    path('leave/', views.leave_request, name='leave_request_list'),
    path('api/leave/', LeaveRequestAPIView.as_view(), name='leave-request-api'),
]