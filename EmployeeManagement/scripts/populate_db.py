from application.models import User


def zbraz():
    User.objects.all().delete()

def run():
    zbraz()