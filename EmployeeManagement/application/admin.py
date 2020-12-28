from django.contrib import admin

from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','gender','birthday','join_date','email','phone','leave_days','department','flag')
admin.site.register(User,UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Role,RoleAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parentDepartment_id')
admin.site.register(Department,DepartmentAdmin)