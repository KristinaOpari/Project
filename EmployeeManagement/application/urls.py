from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
        path(r'create/', views.create_view),



]
