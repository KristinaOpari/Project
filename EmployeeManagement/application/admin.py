from django.contrib import admin

from .models import *
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname','gender','birthday','join_date','primary_email','secondary_email','phone','leave_days_available','department','is_active')
admin.site.register(User,UserAdmin)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Role,RoleAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'parentDepartment_id')
admin.site.register(Department,DepartmentAdmin)

class LeaveAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'start','end','duration','status','approver')
admin.site.register(Leave,LeaveAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ('user_id','password')
admin.site.register(Account,AccountAdmin)

class UserRoleAdmin(admin.ModelAdmin):
    list_display =('user_id','role_id')
admin.site.register(UserRole,UserRoleAdmin)