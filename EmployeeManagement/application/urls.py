from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'departments',views.DepartmentViewSet,basename='department')
router.register(r'leaveapply',views.LeaveApplyViewSet,basename='leaveapply')
router.register(r'leaveapprove', views.LeaveApproveViewSet, basename='leaveapprove')
router.register(r'holidays', views.HolidaysViewSet,basename='holiday')
router.register(r'roles',views.RolesViewSet,basename='role')
router.register(r'userroles', views.UserRoleViewSet,basename='userrole')

urlpatterns=[
        path('',include(router.urls)),
        path('export/users/excel', views.export_users_excel, name='export_excel_users'),
        path('export/leaves/excel', views.export_leave_request_excel, name='export_excel_leaves'),
        path('export/users/pdf',views.export_users_pdf,name='export_users_pdf'),
        path('export/leaves/pdf',views.export_leaves_pdf,name='export_leaves_pdf'),
        path('api/change-password/', views.ChangePasswordView.as_view(), name='change-password'),

]