from app.simple_pages.models import User

def create_user(form_data):
    # Create new User 
    new_user = User(
        username=form_data.get('username'),
        password=form_data.get('password')
    )
    new_user.save()