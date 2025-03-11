from db.models import User


def create_user(username, password, email=None, first_name=None, last_name=None):
    user = User.objects.create_user(username=username, password=password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
    return user

def get_user(user_id):
    return User.objects.filter(id=user_id).first()

def update_user(user_id, username=None, password=None, email=None, first_name=None, last_name=None):
    user = User.objects.filter(id=user_id).first()
    if not user:
        return None
    if username:
        user.username = username
    if password:
        user.set_password(password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
    return user