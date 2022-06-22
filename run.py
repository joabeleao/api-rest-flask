'''
Filename: instance.py
Version: 1.0
Author: joabe leão - joabe.leao1@gmail.com

Description:
    App creation, description and instance
'''
from app import app

from flask_swagger_ui import get_swaggerui_blueprint


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=2222)


### swagger specific ###
SWAGGER_URL = '/api/v1/docs'
API_URL = '/static/docs.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "API-Python-Flask-REST"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

