
from .resources import *
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets, status

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response(data='User deleted')

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class=DepartmentSerializer
    queryset=Department.objects.all()


class LeaveApplyViewSet(viewsets.ModelViewSet):
    serializer_class=LeaveApplySerializer
    queryset=Leave.objects.all()

class LeaveApproveViewSet(viewsets.ModelViewSet):
    serializer_class=LeaveApproveSerializer
    queryset=Leave.objects.all()

    def list(self, request ,*args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request,*args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset=Account.objects.all()

class UserRoleViewSet(viewsets.ModelViewSet):
    serializer_class = UserRoleSerializer
    queryset=UserRole.objects.all()

class HolidaysViewSet(viewsets.ModelViewSet):
    serializer_class=HolidaysSerializer
    queryset=Holidays.objects.all()

def export_users_excel(request):
    users_resource = UserResource()
    dataset = users_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    return response

def export_leave_request_excel(request):
    leaves_resource = LeaveResource()
    dataset = leaves_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="leave_requests.xls"'
    return response

def export_users_pdf(request):
    template_path = 'pdf1.html'
    queryset = User.objects.all()
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