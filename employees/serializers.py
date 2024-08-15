from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Employee
        fields = ['id', 'name', 'department', 'email', 'phone', 'username', 'password']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create(username=username, password=password)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee
