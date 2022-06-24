'''
User creation and information
'''
from werkzeug.security import generate_password_hash
from flask import request
from flask import jsonify

from app import db
from app.models.users import Users
from app.models.users import user_schema
from app.models.users import users_schema

def post_user():
    '''
    doc
    '''
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']
    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    if query_user(username):
        return jsonify({'message': 'Username already exists'}), 400
    if query_email(email):
        return jsonify({'message': 'Email already exists'}), 400

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'User successfully registred', 'data': result}), 201
    except Exception:
        return jsonify({'message': 'unable to create', 'data': {}}), 500

def update_user(user_id):
    '''
    doc
    '''
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(user_id)

    if not user:
        return jsonify({'message': 'user not found', 'data': {}}), 404
    if query_user(username):
        return jsonify({'message': 'Unable to update. Unavailable username'}), 400
    if query_email(email):
        return jsonify({'message': 'Unable to update. Unabailable e-mail'}), 400

    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email

        db.session.commit()

        result = user_schema.dump(user)
        return jsonify({'message': 'User successfully updated', 'data': result}), 200

    except Exception:
        return jsonify({'message': 'Unable to update', 'data': {}}), 500

def delete_user(user_id):
    '''
       Delete a user according to a given id
    '''
    user = Users.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found', 'data': {}}), 404

    if user:
        try:
            db.session.delete(user)
            db.session.commit()

            result = user_schema.dump(user)
            return jsonify({'message': 'User successifully deleted', 'data': result}), 200

        except Exception:
            return jsonify({'message': 'Unable to delete', 'data': {}}), 500

    return jsonify({'message': 'Unable to delete', 'data': {}}), 500

def get_users():
    '''
       List information about all available users on database
    '''
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'Successfully feched', 'data': result}), 200

    return jsonify({'message': 'Unable to get data', 'data': {}}), 500

def get_user(user_id):
    '''
       List information about a specific user according to a given id
    '''
    user = Users.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found', 'data': {}}), 404

    if user:
        result = user_schema.dump(user)
        return jsonify({'message': 'Successfully feched', 'data': result}), 200

    return jsonify({'message': 'Unable to get data', 'data': {}}), 500

def query_user(username):
    '''
       Verify the user exists on database according to the given username
    '''
    try:
        return Users.query.filter(Users.username == username).one()
    except Exception:
        return None

def query_email(email):
    '''
       Verify the e-mail exists on database according to the given e-mail
    '''
    try:
        return Users.query.filter(Users.email == email).one()
    except Exception:
        return None
