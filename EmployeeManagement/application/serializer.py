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

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields='__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'

class AcountSerializers(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields='__all__'

class HolidaysSeriializer(serializers.ModelSerializer):
    class Meta:
        model=Holidays
        fields='__all__'

