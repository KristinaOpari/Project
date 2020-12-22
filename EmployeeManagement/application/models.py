from django.db import models


class User(models.Model): #Shiko users ne django doc
    CHOICES_GENDER=(
        ('F', 'Female'),
        ('M', 'Male')
    )
    CHOICES_ENABLE=(
        ('1','Enabled'),
        ('0', 'Disabled')
    )
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)
    birthday=models.DateField()
    join_date=models.DateField()
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    leave_days = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, blank=True, null=True)
    flag=models.CharField(max_length=4, choices=CHOICES_ENABLE,default='1')


class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    parentDepartment_id = models.ForeignKey('Department', on_delete=models.CASCADE)

class Leave(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date = models.DateField()
    total_days=models.IntegerField()
    reason=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    approver=models.CharField(max_length=255)

class Role(models.Model):
    role_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)


class UserRole(models.Model):
    user_role_id=models.IntegerField(primary_key=True)
    role_id=models.ForeignKey(Role, on_delete=models.CASCADE)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

class Account(models.Model):
    account_id=models.IntegerField(primary_key=True)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    password=models.CharField(max_length=50)

class Holidays(models.Model):
    holiday_id=models.IntegerField(primary_key=True)
    date=models.DateField()
    name=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    last_active=models.DateField()