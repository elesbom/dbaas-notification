# coding: utf-8
from dbaas_notification.views import UserTasks


def add_url_rules(app):
    app.add_url_rule(
        '/<username>/tasks',
        view_func=UserTasks.as_view('user_tasks'),
        methods=['GET', 'POST'])
