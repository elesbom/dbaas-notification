from flask import Flask
# from flask_redis import FlaskRedis
from dbaas_notification.router import add_url_rules
from flask_redis import Redis

flask_app = Flask("dbaas_notification")
flask_app.config['REDIS_URL'] = 'redis://:EMSgrxGPby@dbaasnotif-01-150040581922.dev.redis.globoi.com:6379/0'
flask_app.config['REDIS_HOST'] = 'dbaasnotif-01-150040581922.dev.redis.globoi.com'
flask_app.config['REDIS_PORT'] = 6379
flask_app.config['REDIS_DB'] = 0
flask_app.config['REDIS_PASSWORD'] = 'EMSgrxGPby'
add_url_rules(flask_app)
redis_store = Redis(flask_app)


@flask_app.route('/healthcheck/')
def healthcheck():
    return 'WORKING'
