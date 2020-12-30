from django.db import models
import numpy as np
class User(models.Model):
    CHOICES_GENDER=(
        ('F', 'Female'),
        ('M', 'Male')
    )

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    birthday=models.DateField()
    join_date=models.DateField()
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    leave_days_available = models.IntegerField(default=28)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    parentDepartment_id = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    supervisor=models.ForeignKey('UserRole', on_delete=models.CASCADE, default="", blank=True, null=True,limit_choices_to={"role_id":2}) #limit_choices_to
    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    role_id=models.ForeignKey(Role,on_delete=models.CASCADE,default=1)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)

class Leave(models.Model):
    LEAVE_STATUS_APPROVED = 1
    LEAVE_STATUS_REJECTED = 2
    LEAVE_STATUS_PENDING = 3
    LEAVE_STATUS_CHOICES = (
        (LEAVE_STATUS_APPROVED, 'approved'),
        (LEAVE_STATUS_REJECTED, 'rejected'),
        (LEAVE_STATUS_PENDING, 'pending'),
    )
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    start=models.DateTimeField()
    end= models.DateTimeField()
    reason=models.CharField(max_length=255)
    status=models.CharField(max_length=255,blank=True, null=True,choices=LEAVE_STATUS_CHOICES,default=LEAVE_STATUS_PENDING)
    approver=models.ForeignKey(User,on_delete=models.CASCADE, related_name='approver',blank=True,null=True)

    @property
    def duration(self):
        if self.start.date() == self.end.date():
            duration=self.end - self.start
            return "{} hours {} minutes ".format(duration.seconds//3600,(duration.seconds//60)%60)
        else:
            duration=np.busday_count(self.start.strftime("%Y-%m-%d"),self.end.strftime("%Y-%m-%d"))
            return "{} days".format(duration)

class Account(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    password = models.CharField(max_length=50)

class Holidays(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    last_active = models.DateField()