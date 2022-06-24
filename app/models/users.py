'''
Database models creation
'''
import datetime

from app import db
from app import ma

class Users(db.Model):
    '''
        User's table, class and field definition
    '''
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(60), unique=True,nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

class UsersSchema(ma.Schema):
    '''
        Setting Marshmallow scheme to make json usage easier
    '''
    class Meta:
        '''
            Database fieds
            Since using marshmallow with SQLAlchemy a meta class must be created
            It will use the filds created on model above
        '''
        fields = ('id', 'username', 'name', 'email', 'password', 'created_on')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True) # many = array
