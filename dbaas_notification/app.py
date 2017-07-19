import os
from flask import Flask
from dbaas_notification.router import add_url_rules
from flask_redis import Redis

flask_app = Flask("dbaas_notification")
flask_app.config['REDIS_HOST'] = os.getenv('REDIS_HOST')
flask_app.config['REDIS_PORT'] = os.getenv('REDIS_PORT', 6379)
flask_app.config['REDIS_DB'] = os.getenv('REDIS_DB', 0)
flask_app.config['REDIS_PASSWORD'] = os.getenv('REDIS_PASSWORD')
add_url_rules(flask_app)
redis_store = Redis(flask_app)


@flask_app.route('/healthcheck/')
def healthcheck():
    return 'WORKING'
