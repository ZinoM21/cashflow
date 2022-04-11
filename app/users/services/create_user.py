from app.users.models import User

def create_user(form_data):
    # Create new User 
    new_user = User(
        email=form_data.get('email'),
        password=form_data.get('password')
    )
    new_user.save()