from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'departments',views.DepartmentViewSet,basename='department')
router.register(r'leaves',views.LeaveViewSet,basename='leave')
router.register(r'accounts',views.AccountViewSet,basename='account')
urlpatterns=[
        path('',include(router.urls)),
]