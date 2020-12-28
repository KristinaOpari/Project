from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns=[
        path(r'create-User/',views.createUser),
        path(r'update-user/<str:pk>/',views.updateUser),
        path(r'delete-user/<str:pk>/',views.deleteUser),
        path(r'show-users/',views.showUser),
        path('',include(router.urls)),



]
