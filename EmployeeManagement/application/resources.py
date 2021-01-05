from import_export import resources, fields, widgets
from .models import *

class UserResource(resources.ModelResource):
    name= fields.Field(attribute='name',column_name=(u'Name'))
    surname = fields.Field(attribute='surname', column_name=(u'Surname'))
    primary_email = fields.Field(attribute='primary_email', column_name=(u'Primary Email'))
    secondary_email = fields.Field(attribute='secondary_email', column_name=(u'Secondary Email'))
    birthday = fields.Field(attribute='birthday', column_name=(u'Birthday'))
    phone = fields.Field(attribute='phone', column_name=(u'Telephone Number'))
    join_date = fields.Field(attribute='join_date', column_name=(u'Date Joined'))
    gender = fields.Field(attribute='get_gender_display',column_name=(u'Gender'))
    leave_days_available=fields.Field(attribute='leave_days_available',column_name=(u'Leave Days Available'))
    department=fields.Field(attribute='department__name',column_name=(u'Department'))
    is_active=fields.Field(attribute='is_active', column_name=(u'Active'),widget=widgets.BooleanWidget())
    class Meta:
        model = User
        export_order = ('id', 'name', 'surname', 'gender','birthday','primary_email','secondary_email','phone','join_date','leave_days_available','department','is_active')

class LeaveResource(resources.ModelResource):
    user_id=fields.Field(attribute='user_id__name',column_name=(u'Name'))
    user_surname=fields.Field(attribute='user_id__surname',column_name=(u'Surname'))
    user_email = fields.Field(attribute='user_id__primary_email', column_name=(u'Email'))
    status = fields.Field(attribute='get_status_display',column_name=(u'Status') )
    approver_name = fields.Field(attribute='approver__name', column_name=(u'Approver Name'))
    approver_surname = fields.Field(attribute='approver__surname', column_name=(u'Approver Surname'))
    start=fields.Field(attribute='start',column_name=(u'Start of Leave'))
    end=fields.Field(attribute='end',column_name=(u'End of Leave'))
    duration=fields.Field(column_name=(u'Duration'))
    class Meta:
        model=Leave
        exclude=['approver']
        export_order=('id','user_id','user_surname','user_email','start','end','duration','reason','status','approver_name','approver_surname')

    def dehydrate_duration(self, obj):
        return obj.duration