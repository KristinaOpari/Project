import datetime

from application.models import User,Department,Role, Holidays
import csv


def populate_roles_by_user():
    if Role.objects.all().count() == 0:
        with open('roles.csv', 'r', encoding='utf8') as data:
            reader=csv.reader(data)
            for line in reader:
                role=line[0]
                Role(
                    name=role
                ).save()
'''
With the function below populate_holidays i am going to populate the holidays model using the csv file holidays.csv which contains all the
holidays in Albania. Firstly I read the csv file and assign each 'element' of the line at the specific field of the holidays table and create a object of holidays.
Once this part is finished, since in Albania there is a rule that when a holidays is a Sunday or a Saturday, Monday is off, and when two holidays are Saturday and Sunday consecuently, Monday and Tuesday are off.
So after all actual holidays are created, we have to create these other holidays and this is done by iterating through all the already 
created objects and check some conditions. If the holiday is a Sunday it has two options, to check whether the previous holiday was a Saturday and if true to
create the other object with the day on Tuesday and if not it will create the other object with the day on Monday. Otherwise if the holiday is a Saturday it will create directly the other object
with the day on Monday.
'''
def populate_holidays():
    if Holidays.objects.all().count() == 0:

        with open('holidays.csv','r',encoding='utf8') as data:
            reader=csv.reader(data)

            for line in reader:
                date=datetime.datetime.strptime(line[0],"%Y-%m-%d")
                day_of_week=line[1]
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


def delete1():
    Holidays.objects.all().delete()
    Role.objects.all().delete()


def run():
    populate_roles_by_user()
    populate_holidays()
