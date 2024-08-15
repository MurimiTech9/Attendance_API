from django.urls import path
from employees import views
from .views import EmployeeListAPIView, EmployeeDetalAPIView

urlpatterns = [
    path('employees/', views.employee_list, name='employee_list'),
    path('api/employees/', EmployeeListAPIView.as_view(), name='employee-list-api'),
    path('api/employees/<uuid:pk>/', EmployeeDetalAPIView.as_view(), name= 'employee-detail-api'),
    #other URL patterns as needed
]
