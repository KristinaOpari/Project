import datetime

from application.models import User,Department,Role, Holidays
import csv

def populate_roles():
    rol1=Role(
        name="Human Resource"
    )
    rol1.save()
    rol2=Role(
        name="Supervisor"
    )
    rol2.save()
    rol3=Role(
        name="Employee"
    )
    rol3.save()

def populate_roles_by_user():
    with open('roles.csv', 'r', encoding='utf8') as data:
        reader=csv.reader(data)
        for line in reader:
            role=line
            Role(
                name=role
            ).save()

def populate_holidays():
    with open('holidays.csv','r',encoding='utf8') as data:
        days = []
        index=0
        reader=csv.reader(data)

        for line in reader:
            date=datetime.datetime.strptime(line[0],"%Y-%m-%d")
            day_of_week=line[1]
            days.append(day_of_week)
            index+=1
            name=line[2]
            status=line[3]
            Holidays(
                date=date,
                day_of_week=day_of_week,
                name=name,
                status=status
            ).save()
    n=Holidays.objects.all().count()

    for i in range(1,n+1):
        if (Holidays.objects.get(pk=i)).day_of_week == 'Sunday':
            if i==1:
                date1 = (Holidays.objects.get(pk=i)).date
                Holidays(
                    date=date1.replace(day=date1.day + 1),
                    day_of_week='Monday',
                    name=(Holidays.objects.get(pk=i)).name,
                    status=(Holidays.objects.get(pk=i)).status
                ).save()
            else:
                if (Holidays.objects.get(pk=i - 1)).day_of_week == 'Saturday':
                    date1 = (Holidays.objects.get(pk=i)).date
                    Holidays(
                        date=date1.replace(day=date1.day + 2),
                        day_of_week='Tuesday',
                        name=(Holidays.objects.get(pk=i)).name,
                        status=(Holidays.objects.get(pk=i)).status
                    ).save()
                else:
                    date1 = (Holidays.objects.get(pk=i)).date
                    Holidays(
                        date=date1.replace(day=date1.day + 1),
                        day_of_week='Monday',
                        name=(Holidays.objects.get(pk=i)).name,
                        status=(Holidays.objects.get(pk=i)).status
                    ).save()

        elif (Holidays.objects.get(pk=i)).day_of_week == 'Saturday':
            date1 = (Holidays.objects.get(pk=i)).date
            Holidays(
                date=date1.replace(day=date1.day + 2),
                day_of_week='Monday',
                name=(Holidays.objects.get(pk=i)).name,
                status=(Holidays.objects.get(pk=i)).status
            ).save()

def delete():
    User.objects.all().delete()
    Department.objects.all().delete()
    Role.objects.all().delete()

def delete1():
    Holidays.objects.all().delete()
def run():
    populate_roles()
    populate_holidays()