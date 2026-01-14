import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-me'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///mock_server.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False