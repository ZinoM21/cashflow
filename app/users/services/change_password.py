from app.users.models import User
from werkzeug.security import generate_password_hash, check_password_hash

# Change password here:


# def create_user(form_data):
#     # Create new User 
#     new_user = User(
#         email=form_data.get('email'),
#         password=generate_password_hash(form_data.get('password'))
#     )
#     new_user.save()
    
#     return new_user