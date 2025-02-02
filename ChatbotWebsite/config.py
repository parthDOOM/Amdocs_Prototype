# import os

# # Config class to store all the configuration variables


# class Config:
#     DEBUG = False
#     SECRET_KEY = os.environ.get("e374bd42fb1f23eafd682fdddb343ffd")
#     # contain mysql database url with user and password
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
#     # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/users' #mysql
#     # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  #Alternative database if mysql not working
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     MAIL_SERVER = "smtp.gmail.com"
#     MAIL_PORT = 587
#     MAIL_USE_TLS = True
#     MAIL_USE_SSL = False
#     MAIL_USERNAME = os.environ.get("parthivmjasoliya31102@gmail.com")
#     MAIL_PASSWORD = os.environ.get("cxmq fiin haat xaac")
import os

# Config class to store all the configuration variables

class Config:
    DEBUG = True  # Enable DEBUG mode for local development
    SECRET_KEY = "UR_SECRET_KEY"  # Hardcoded for local development
    # MySQL database URL with user and password
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@localhost/users'  # Replace 'your_password' with your MySQL password
    # Alternatively, you can use SQLite for simpler local setup
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail configuration for Gmail
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = "UR_EMAIL"  # Replace with your Gmail
    MAIL_PASSWORD = "UR_PASSWORD"  # Replace with your generated Gmail App Password
