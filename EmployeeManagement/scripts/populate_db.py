from application.models import User,Department,Role
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
            roli=Role(
                name=role
            )
            roli.save()

def delete():
    User.objects.all().delete()
    Department.objects.all().delete()
    Role.objects.all().delete()

def run():
    delete()
    populate_roles()