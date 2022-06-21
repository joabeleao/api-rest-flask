'''
doc
'''
from app import app
from flask import jsonify
from flask import request
from functools import wraps
from werkzeug.security import check_password_hash

from app.views.users import query_user
from app.views.users import get_user

import jwt
import datetime

def token_required(f):
    '''
    Doc
    '''
    @wraps(f)
    def decorated(*args, **kwargs):
        '''
        Doc
        '''
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            return jsonify({'message': 'token is invalid or missing', 'data': {} }), 401

        if not token:
            return jsonify({'message': 'token is missing', 'data': {} }), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = query_user(username=data['username'])
        except:
            return jsonify({'message': 'token is invalid or expired', 'data': {} }), 401
        return f(current_user.username, *args, **kwargs)
    return decorated

def auth():
    '''
    Doc
    '''
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="login and password required"'}), 401

    user = query_user(auth.username)
    if not user:
        return jsonify({'message': 'user not found', 'data': {} }), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12) }, app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'Invalid username or password', 'WWW-Authenticate': 'Basic auth=Login required'}), 401
