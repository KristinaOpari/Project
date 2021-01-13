from django.db.models import Q
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='name',allow_null=True)

    class Meta:
        model=SystemUser
        fields=["first_name","last_name","password","gender","birthday","email","secondary_email","phone","is_active","is_staff","is_HR","is_Supervisor","is_Employee","leave_days_available","department","user_permissions"]
        read_only_fields=['groups','date_joined','last_login','is_superuser']


    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = SystemUser

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class DepartmentSerializer(serializers.ModelSerializer):
    parentDepartment_id=serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='name',allow_null=True)
    supervisor=serializers.SlugRelatedField(queryset=SystemUser.objects.filter(is_Supervisor=True), slug_field='first_name',allow_null=True)
    class Meta:
        model=Department
        fields='__all__'

class LeaveApplySerializer(serializers.ModelSerializer):
    duration=serializers.ReadOnlyField()
    approver = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
    status = serializers.ChoiceField(read_only=True,choices=Leave.LEAVE_STATUS_CHOICES, source='get_status_display')
    user_id = serializers.SlugRelatedField(read_only=True, slug_field='first_name')

    class Meta:
        model=Leave
        fields='__all__'
        read_only_fields = ('approver','status','duration','user_id')


class LeaveApproveSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=Leave.LEAVE_STATUS_CHOICES, source='get_status_display')
    approver = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
    user_id = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
    class Meta:
        model=Leave
        fields="__all__"
        read_only_fields=('user_id','start','end','reason','approver')

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

