import os
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import BackgroundScheduler

# SQLAlchemy
db = SQLAlchemy()

# APScheduler
scheduler = BackgroundScheduler(daemon=True)
weeklyJobName = 'weekly_job'
playerAlarmName = 'player_alarm'

# Данные о сообществе
album_id = int(os.environ.get('ALBUM_ID'))  #  id альбома с мемами для send_blame_message