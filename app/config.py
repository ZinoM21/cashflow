from os import environ
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')

SQLALCHEMY_TRACK_MODIFICATIONS = False