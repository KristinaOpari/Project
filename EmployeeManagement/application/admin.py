from django.contrib import admin

from .models import *
class UserAdmin(admin.ModelAdmin):
    fields= ('first_name','last_name','gender','birthday','date_joined','email','secondary_email','phone','leave_hours_available', 'department', 'is_active','is_staff','is_superuser','is_HR','is_Supervisor','is_Employee','user_permissions','groups','password')

admin.site.register(SystemUser,UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Role,RoleAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parentDepartment_id')
admin.site.register(Department,DepartmentAdmin)

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'start','end','duration','status','approver')
admin.site.register(Leave,LeaveAdmin)


class UserRoleAdmin(admin.ModelAdmin):
    list_display =('user_id','role_id')
admin.site.register(UserRole,UserRoleAdmin)