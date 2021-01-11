from import_export import resources, fields, widgets
from .models import *

class UserResource(resources.ModelResource):
    first_name= fields.Field(attribute='first_name',column_name=(u'Name'))
    last_name = fields.Field(attribute='last_name', column_name=(u'Surname'))
    email = fields.Field(attribute='email', column_name=(u'Primary Email'))
    secondary_email = fields.Field(attribute='secondary_email', column_name=(u'Secondary Email'))
    birthday = fields.Field(attribute='birthday', column_name=(u'Birthday'))
    phone = fields.Field(attribute='phone', column_name=(u'Telephone Number'))
    date_joined = fields.Field(attribute='date_joined', column_name=(u'Date Joined'))
    gender = fields.Field(attribute='get_gender_display',column_name=(u'Gender'))
    leave_days_available=fields.Field(attribute='leave_days_available',column_name=(u'Leave Days Available'))
    department=fields.Field(attribute='department__name',column_name=(u'Department'))
    is_active=fields.Field(attribute='is_active', column_name=(u'Active'),widget=widgets.BooleanWidget())
    class Meta:
        model = SystemUser
        export_order = ('id', 'first_name', 'last_name', 'gender','birthday','email','secondary_email','phone','date_joined','leave_days_available','department','is_active')

class LeaveResource(resources.ModelResource):
    user_id=fields.Field(attribute='user_id__first_name',column_name=(u'Name'))
    user_surname=fields.Field(attribute='user_id__last_name',column_name=(u'Surname'))
    user_email = fields.Field(attribute='user_id__email', column_name=(u'Email'))
    status = fields.Field(attribute='get_status_display',column_name=(u'Status') )
    approver_name = fields.Field(attribute='approver__first_name', column_name=(u'Approver Name'))
    approver_surname = fields.Field(attribute='approver__last_name', column_name=(u'Approver Surname'))
    start=fields.Field(attribute='start',column_name=(u'Start of Leave'))
    end=fields.Field(attribute='end',column_name=(u'End of Leave'))
    duration=fields.Field(column_name=(u'Duration'))
    class Meta:
        model=Leave
        exclude=['approver']
        export_order=('id','user_id','user_surname','user_email','start','end','duration','reason','status','approver_name','approver_surname')

    def dehydrate_duration(self, obj):
        return obj.duration