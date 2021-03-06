'''
Filename: instance.py
Version: 1.0
Author: joabe leão - joabe.leao1@gmail.com

Description:
    App creation, description and instance
'''
import random
import string

random_str = string.ascii_letters + string.digits + string.ascii_uppercase
key = ''.join(random.choice(random_str) for i in range(12))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/datatodash'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = key
