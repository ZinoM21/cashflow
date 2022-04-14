from flask import redirect, url_for
from flask_login import LoginManager
from app.users.models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    
    return redirect(url_for('users.get_login'))