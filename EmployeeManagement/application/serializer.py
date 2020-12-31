
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class LeaveApplySerializer(serializers.ModelSerializer):
    duration=serializers.ReadOnlyField()
    class Meta:
        model=Leave
        fields='__all__'
        read_only_fields = ['approver','status']

class LeaveApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields='__all__'
        read_only_fields=['user_id','start_date','end_date','reason']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRole
        fields='__all__'

class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Holidays
        fields='__all__'

