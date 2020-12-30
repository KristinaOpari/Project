from django.http import Http404
from rest_framework.response import Response

from .models import *
from .serializer import *
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404, redirect

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='User deleted')

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()


class LeaveApplyViewSet(viewsets.ModelViewSet):
    serializer_class=LeaveApplySerializer
    queryset=Leave.objects.all()

class LeaveApproveViewSet(viewsets.ModelViewSet):
    serializer_class=LeaveApproveSerializer
    queryset=Leave.objects.all()

    def list(self, request ,*args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request,*args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=Account.objects.all()

