from os import environ
from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
load_dotenv()