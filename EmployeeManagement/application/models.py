from django.contrib.auth.base_user import BaseUserManager
from django.db import models
import numpy as np
from django.contrib.auth.models import AbstractUser
from django.db.models import Q


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class SystemUser(AbstractUser):
    objects = UserManager()
    CHOICES_GENDER=(
        ('F', 'Female'),
        ('M', 'Male')
    )
    username= None
    email = models.EmailField( unique=True)
    secondary_email = models.EmailField(unique=True, default="")
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    birthday=models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    leave_days_available = models.IntegerField(default=28)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    is_HR=models.BooleanField(default=False)
    is_Supervisor=models.BooleanField(default=False)
    is_Employee=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super(SystemUser, self).save(*args, **kwargs)
        if(self.is_HR):
            if UserRole.objects.filter(Q(role_id=1) & Q(user_id=self)).exists():
                pass
            else:
                UserRole.objects.create(user_id=self, role_id=Role.objects.get(pk=1))
        if(self.is_Supervisor):
            if UserRole.objects.filter(Q(role_id=2) & Q(user_id=self)).exists():
                pass
            else:
                UserRole.objects.create(user_id=self, role_id=Role.objects.get(pk=2))
        if(self.is_Employee):
            if UserRole.objects.filter(Q(role_id=3) & Q(user_id=self)).exists():
                pass
            else:
                UserRole.objects.create(user_id=self, role_id=Role.objects.get(pk=3))




class Department(models.Model):
    name = models.CharField(max_length=255)
    parentDepartment_id = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    supervisor=models.ForeignKey('SystemUser', on_delete=models.CASCADE, related_name='supervisor',default="", blank=True, null=True)
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

    def deduct_leave_days(self):
        if self.status == 'A':
            user = SystemUser.objects.get(pk=self.user_id.id)
            nrdigits=0
            digit=0
            for ch in self.duration:
                if ch.isdigit():
                    digit=int(ch)
                    nrdigits+=1
            if nrdigits == 1:
                user.leave_days_available = user.leave_days_available - digit
                user.save()

class Holidays(models.Model):
    date = models.DateField()
    day_of_week=models.CharField(max_length=255,default="")
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
