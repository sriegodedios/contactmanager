from register.models import RegisteredUser


def email_present(email):
    if RegisteredUser.objects.filter(email=RegisteredUser.Email).exists():
        return True

    return False