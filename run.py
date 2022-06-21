'''
Filename: instance.py
Version: 1.0
Author: joabe leão - joabe.leao1@gmail.com

Description:
    App creation, description and instance
'''
from app import app

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=2222)
