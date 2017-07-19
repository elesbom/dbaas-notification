# coding: utf-8
import os

from dbaas_notification.app import flask_app

PORT = os.getenv('PORT', 5001)
flask_app.run(port=int(PORT), host='0.0.0.0', debug=True)
