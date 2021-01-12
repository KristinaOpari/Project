from django.db.models import Q
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=SystemUser.CHOICES_GENDER, source='get_gender_display')
    department = serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='name')

    class Meta:
        model=SystemUser
        fields='__all__'
        read_only_fields=['groups','date_joined','last_login','is_superuser','is_staff']


    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class DepartmentSerializer(serializers.ModelSerializer):
    parentDepartment_id=serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='name')
    supervisor=serializers.SlugRelatedField(queryset=SystemUser.objects.filter(is_Supervisor=True), slug_field='first_name')
    class Meta:
        model=Department
        fields='__all__'

class LeaveApplySerializer(serializers.ModelSerializer):
    duration=serializers.ReadOnlyField()
    approver = serializers.SlugRelatedField(read_only=True, slug_field='first_name')
    status = serializers.ChoiceField(read_only=True,choices=Leave.LEAVE_STATUS_CHOICES, source='get_status_display')

    class Meta:
        model=Leave
        fields='__all__'
        read_only_fields = ['approver','status','duration']

class LeaveApproveSerializer(serializers.ModelSerializer):
    approver = serializers.SlugRelatedField(queryset=SystemUser.objects.filter(Q(is_Supervisor=True) | Q(is_HR=True)), slug_field='first_name')
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

