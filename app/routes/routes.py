'''
Endpoint settings
'''
from flask import redirect
from flask import abort

from app import app
from app.views.users import get_users
from app.views.users import get_user
from app.views.users import delete_user
from app.views.users import post_user
from app.views.users import update_user
from app.views.helper import auth
from app.views.helper import token_required

@app.route('/', methods=['GET'])
def root():
    '''
    doc
    '''
    return redirect('/api/v1/docs')

@app.route('/doc', methods=['GET'])
def doc():
    '''
    doc
    '''
    return redirect('/api/v1/docs')

@app.route('/docs', methods=['GET'])
def docs():
    '''
    doc
    '''
    return redirect('/api/v1/docs')

@app.route('/api/v1/users', methods=['POST'])
@token_required
def user_post(user):
    '''
    Doc
    '''
    if user != 'admin':
        abort(404)

    return post_user()

@app.route('/api/v1/users', methods=['GET'])
@token_required
def user_get(user):
    '''
    Doc
    '''
    if user != 'admin':
        abort(404)

    return get_users()

@app.route('/api/v1/users/<id>', methods=['GET'])
@token_required
def userid_get(user, user_id):
    '''
    Doc
    '''
    if user != 'admin':
        abort(404)

    return get_user(user_id)

@app.route('/api/v1/users/<id>', methods=['PUT'])
@token_required
def user_update(user, user_id):
    '''
    Doc
    '''
    if user != 'admin':
        abort(404)

    return update_user(user_id)

@app.route('/api/v1/users/<id>', methods=['DELETE'])
@token_required
def userid_delete(user, user_id):
    '''
    Doc
    '''
    if user != 'admin':
        abort(404)

    return delete_user(user_id)

@app.route('/api/v1/auth', methods=['POST'])
def authenticate():
    '''
    Doc
    '''
    return auth()
