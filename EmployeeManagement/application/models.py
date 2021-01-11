from django.db import models
import numpy as np
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractUser


class SystemUser(AbstractUser):
    CHOICES_GENDER=(
        ('F', 'Female'),
        ('M', 'Male')
    )

    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    birthday=models.DateField(blank=True,null=True)
    secondary_email = models.EmailField(unique=True,default="")
    phone = models.CharField(max_length=255,blank=True,null=True)
    leave_days_available = models.IntegerField(default=28)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    is_HR=models.BooleanField(default=False)
    is_Supervisor=models.BooleanField(default=False)
    is_Employee=models.BooleanField(default=True)

    REQUIRED_FIELDS= ['email']
    def __str__(self):
        return self.first_name

    # def save(self, *args, **kwargs):
    #     super(User, self).save(*args, **kwargs)
    #     account=Account.objects.create(user_id=self, password="ikub1234")
    #     # send_mail(
    #     #     'Account Activated',
    #     #     'Please activate you account using: Email: ({}) Password:({})'.format(self.primary_email, account.password),
    #     #     'noreply@gmail.com',
    #     #     ['{}'.format(self.email)],
    #     #     fail_silently=False
    #     #
    #     # )

class Department(models.Model):
    name = models.CharField(max_length=255)
    parentDepartment_id = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    supervisor=models.ForeignKey('SystemUser', on_delete=models.CASCADE, related_name='supervisor',default="", blank=True, null=True) #limit_choices_to
    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    role_id=models.ForeignKey(Role,on_delete=models.CASCADE,default=1)
    user_id=models.ForeignKey(SystemUser,on_delete=models.CASCADE,default=1)

class Leave(models.Model):

    LEAVE_STATUS_CHOICES = (
        ('A', 'Approved'),
        ('R','Rejected'),
        ('P', 'Pending'),
    )
    user_id=models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    start=models.DateTimeField()
    end= models.DateTimeField()
    reason=models.CharField(max_length=255)
    status=models.CharField(max_length=255,blank=True, null=True,choices=LEAVE_STATUS_CHOICES,default='P')
    approver=models.ForeignKey(SystemUser,on_delete=models.CASCADE, related_name='approver',blank=True,null=True)

    @property
    def duration(self):
        if self.start.date() == self.end.date():
            duration=self.end - self.start
            return "{} hours {} minutes ".format(duration.seconds//3600,(duration.seconds//60)%60)
        else:
            duration=np.busday_count(self.start.strftime("%Y-%m-%d"),self.end.strftime("%Y-%m-%d"))
            return "{} days".format(duration)



class Holidays(models.Model):
    date = models.DateField()
    day_of_week=models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
