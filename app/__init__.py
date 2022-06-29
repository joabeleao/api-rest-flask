'''
Filename: instance.py
Version: 1.0
Author: joabe leão - joabe.leao1@gmail.com

Description:
    App creation, description and instance
'''
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from waitress import serve

app = Flask(__name__)
app.config.from_object('config')
# cors
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

db = SQLAlchemy(app) # db iteration
ma = Marshmallow(app) # convert db info to json

from .models import users 
from .routes import routes # perguntar gunasper sobre recursividade aq
