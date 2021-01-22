
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer, AdminRenderer, JSONRenderer, BrowsableAPIRenderer

from .permissions import IsEmployee, IsHr, IsSupervisor
from .resources import *
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets, status, generics, authentication
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes=[AdminRenderer]
    permission_classes = (IsAuthenticated,IsHr, )

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'update':
            serializer_class=UserUpdateSerializer

        return serializer_class

    def get_queryset(self):
        if self.request.user.is_HR:
            self.queryset = SystemUser.objects.all()
        elif self.request.user.is_Supervisor:
            self.queryset = SystemUser.objects.filter(department=self.request.user.department)
        elif self.request.user.is_Employee:
            self.queryset = SystemUser.objects.filter(id=self.request.user.id)
        return self.queryset

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            self.permission_classes=[IsAuthenticated,IsHr, ]
        elif self.action == 'list':
            if self.request.user.is_HR:
                self.permission_classes = [IsAuthenticated, IsHr, ]
            elif self.request.user.is_Supervisor:
                self.permission_classes = [IsAuthenticated, IsSupervisor, ]
            elif self.request.user.is_Employee:
                self.permission_classes = [IsAuthenticated,IsEmployee, ]
        return super(self.__class__, self).get_permissions()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='User deleted')


class ChangePasswordView(generics.UpdateAPIView):

    serializer_class = ChangePasswordSerializer
    model = SystemUser
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]
    permission_classes = (IsAuthenticated,IsHr,)

    def get_permissions(self):
        if(self.request.user.is_Supervisor):
            self.permission_classes=(IsAuthenticated,IsSupervisor,)
        return super(self.__class__, self).get_permissions()



class LeaveViewSet(viewsets.ModelViewSet):

    authentication_classes = (authentication.SessionAuthentication,)
    serializer_class = LeaveSerializerCreate
    renderer_classes = [AdminRenderer]
    permission_classes = (IsAuthenticated,IsHr)

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = LeaveSerializerUpdate
        if self.action== "list":
            serializer_class=LeaveSerializerList

        return serializer_class
    def get_queryset(self):
        if self.request.user.is_HR :
            self.queryset = Leave.objects.filter(Q(status="P") & Q(user_id__is_Supervisor= True) )
        elif self.request.user.is_Supervisor:
            self.queryset = Leave.objects.filter(Q(user_id__department=self.request.user.department) & Q(status="P") )

        return self.queryset

    def get_permissions(self):
        if self.action == 'create':
            if self.request.user.is_HR:
                self.permission_classes = [IsAuthenticated, IsHr, ]
            elif self.request.user.is_Supervisor:
                self.permission_classes = [IsAuthenticated,IsSupervisor, ]
            elif self.request.user.is_Employee:
                self.permission_classes = [IsAuthenticated,IsEmployee, ]
        elif self.action == 'update'  or self.action == 'retrieve' or self.action == 'list' or self.action == 'destroy':
            if self.request.user.is_HR:
                self.permission_classes = [IsAuthenticated, IsHr, ]
            elif self.request.user.is_Supervisor:
                self.permission_classes = [IsAuthenticated,IsSupervisor, ]

        return super(self.__class__, self).get_permissions()


    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    def perform_update(self, serializer):
        serializer.save(approver=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance.deduct_leave_hours()
        return Response(serializer.data)


class LeaveListView(generics.ListAPIView):
    serializer_class = LeaveSerializerList
    model = Leave
    permission_classes = (IsAuthenticated,)
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]
    def get_queryset(self):
        self.queryset=Leave.objects.filter(user_id=self.request.user.id)
        return self.queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserRoleViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    queryset=UserRole.objects.all()
    permission_classes = (IsAuthenticated,IsHr, )
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]

class HolidaysViewSet(viewsets.ModelViewSet):
    serializer_class=HolidaysSerializer
    queryset=Holidays.objects.all()
    permission_classes = (IsAuthenticated,IsHr, )
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]
    def create(self, request,*args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



class RolesViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    permission_classes = (IsAuthenticated,IsHr, )
    authentication_classes = (authentication.SessionAuthentication,)
    renderer_classes = [AdminRenderer]
    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


def export_users_excel(request):
    users_resource = UserResource()
    dataset = users_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    return response

def export_leave_request_excel(request):
    leaves_resource = LeaveResource()
    dataset = leaves_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="leave_requests.xls"'
    return response

def export_users_pdf(request):
    template_path = 'pdf1.html'
    queryset = SystemUser.objects.all()
    context = {'queryset': queryset}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="user_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def export_leaves_pdf(request):
    template_path = 'pdf2.html'
    queryset = Leave.objects.all()
    context = {'queryset': queryset}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="leave_request_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response