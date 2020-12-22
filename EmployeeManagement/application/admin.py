from django.contrib import admin

from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'surname','gender','birthday','join_date','email','phone','leave_days','department','flag')
admin.site.register(User,UserAdmin)
