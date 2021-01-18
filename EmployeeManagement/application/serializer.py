from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(queryset=Department.objects.all(), slug_field='name',allow_null=True)
    password= serializers.CharField(write_only=True)
    phone=serializers.RegexField(initial= "+355 6XXXXXXXX",regex="^\\+355 6\\d{}$" , max_length=None, min_length=None, allow_blank=False)
    leave_hours_available=serializers.IntegerField(initial=160)


    class Meta:
        model=SystemUser
        fields=["id","first_name","last_name","email","password","gender","birthday","secondary_email","phone","is_active","is_staff","is_HR","is_Supervisor","is_Employee","leave_hours_available","department"]
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

class LeaveSerializer(serializers.ModelSerializer):
    duration=serializers.ReadOnlyField()
    approver = serializers.SlugRelatedField(read_only=True,slug_field='first_name')
    status = serializers.ChoiceField(read_only=True,choices=Leave.LEAVE_STATUS_CHOICES,source='get_status_display')
    user_id = serializers.SlugRelatedField(read_only=True,slug_field='first_name')
    class Meta:
        model=Leave
        fields='__all__'

class LeaveSerializerUpdate(serializers.ModelSerializer):
    approver = serializers.SlugRelatedField(read_only=True,slug_field='first_name')
    status = serializers.ChoiceField(choices=Leave.LEAVE_STATUS_CHOICES, )
    class Meta:
        model=Leave
        fields=['status','approver']

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

