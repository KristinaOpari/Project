from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
        path(r'createUser/', views.create_User),
        path(r'createDepartment/', views.create_Department)



]
