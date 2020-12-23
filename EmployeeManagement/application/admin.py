from django.contrib import admin

from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'surname','gender','birthday','join_date','email','phone','leave_days','department','flag')
admin.site.register(User,UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_id','name')
admin.site.register(Role,RoleAdmin)

class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user_role_id','role_id','user_id')
admin.site.register(UserRole,UserRoleAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_id','name', 'parentDepartment_id', 'supervisor')
admin.site.register(Department,DepartmentAdmin)