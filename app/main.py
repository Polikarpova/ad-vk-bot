from flask import Blueprint, request, json, render_template, make_response
from app.settings import *
import app.messageHandler as MH
from .models import Player
import json
from datetime import datetime, timedelta
from sqlalchemy import desc
from app.extensions import scheduler, playerAlarmName
from app.Notification import Notification

main = Blueprint('main', __name__)


def getNotifications():
    jobs = scheduler.get_jobs(jobstore='default')
    notifications = []

    for job in jobs:
        if job.id.startswith(playerAlarmName):
            date = job.next_run_time + timedelta(hours=3)

            user_id = job.id[len(playerAlarmName):]
            name = Player.query.filter_by(user_id=user_id).first().name

            notifications.append(Notification(name, date))

    return notifications


@main.route('/')
def index():
    players = Player.query.order_by(desc(Player.date)).all()
    notifications = getNotifications()

    context = {
        'players': players,
        'notifications': notifications,
        'minDate': datetime.now() + timedelta(days=1)
    }

    return render_template('base.html', **context)


@main.route('/cron_job', methods=['GET'])
def cron_job():
    make_response("I'm not sleep!")
    return render_template('cron_job.html')


@main.route('/', methods=['POST'])
def processing():
    # Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)

    # Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        # Обрабатываем сообщение
        data['object']['group_id'] = data['group_id']
        print(data['object'])
        MH.process_message(data['object'], token)
        # Сообщение о том, что обработка прошла успешно
        return 'ok'
    elif data['type'] == 'photo_new':
        # добавить фото в бд
        MH.upload_photo_in_database(data['object'])
        return 'ok'

    return 'ok'
