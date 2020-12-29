
from .models import *
from .serializer import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404, redirect

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()

class LeaveViewSet(viewsets.ModelViewSet):
    serializer_class=LeaveSerializer
    queryset=Leave.objects.all()

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=Account.objects.all()

