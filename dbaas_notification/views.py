# coding: utf-8
from flask import json
from flask import request
from flask.views import MethodView


class UserTasks(MethodView):

    def get(self, username):
        from dbaas_notification.app import redis_store
        keys = redis_store.keys("task_users:{}:*".format(username))
        return json.jsonify(redis_store.mget(keys)) if keys else 'Nenhuma Task'

    def post(self, username):
        from dbaas_notification.app import redis_store
        payload = request.data
        task_id = json.loads(payload)['task_id']
        redis_store.set("task_users:{}:{}".format(username, task_id), payload, ex=20)
        return 'ok', 200
