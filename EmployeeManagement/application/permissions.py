from rest_framework.permissions import BasePermission

from .models import SystemUser, Leave


class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_Employee

    def has_object_permission(self, request, view, obj):
        if obj == SystemUser:
            return request.user.is_Employee or obj.id == request.user.id
        elif obj == Leave:
            return request.user.is_Employee or obj.user_id == request.user.id
        return request.user.is_Employee

class IsHr(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_HR

    def has_object_permission(self, request, view, obj):
        if obj == SystemUser:
            return request.user.is_HR or obj.id == request.user.id
        elif obj == Leave:
            return request.user.is_HR or obj.user_id == request.user.id
        return request.user.is_HR

class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_Supervisor

    def has_object_permission(self, request, view, obj):
        if obj == SystemUser:
            return request.user.is_Supervisor or obj.id == request.user.id
        elif obj == Leave:
            return request.user.is_Supervisor or obj.user_id == request.user.id
        return request.user.is_Supervisor


