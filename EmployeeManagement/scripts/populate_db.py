from application.models import User,Department,Role


def populate_roles():
    rol1=Role(
        role_id=1,
        name="Human Resource"
    )
    rol1.save()
    rol2=Role(
        role_id=2,
        name="Supervisor"
    )
    rol2.save()
    rol3=Role(
        role_id=3,
        name="Employee"
    )
    rol3.save()
def zbraz():
    User.objects.all().delete()
    Department.objects.all().delete()
    Role.objects.all().delete()

def run():
    zbraz()
    populate_roles()