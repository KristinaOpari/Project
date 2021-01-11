
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    department= serializers.SlugRelatedField(read_only=True, slug_field='name')
    def get_gender(self, obj):
        return obj.get_gender_display()

    class Meta:
        model=SystemUser
        fields='__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    parentDepartment_id=serializers.SlugRelatedField(read_only=True, slug_field='name')
    supervisor=serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model=Department
        fields='__all__'

class LeaveApplySerializer(serializers.ModelSerializer):
    duration=serializers.ReadOnlyField()
    user_id = serializers.SlugRelatedField(read_only=True, slug_field='name')
    approver = serializers.SlugRelatedField(read_only=True, slug_field='name')
    status = serializers.SerializerMethodField()
    def get_status(self, obj):
        return obj.get_status_display()

    class Meta:
        model=Leave
        fields='__all__'
        read_only_fields = ['approver','status']

class LeaveApproveSerializer(serializers.ModelSerializer):
    class Meta:
        model=Leave
        fields=['status','approver']
        read_only_fields=['user_id','start_date','end_date','reason']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields='__all__'


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRole
        fields='__all__'

class HolidaysSerializer(serializers.ModelSerializer):
    class Meta:
        model=Holidays
        fields='__all__'

