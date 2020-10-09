import app.vk_commands as VKC
import datetime
from app.extensions import db
from app.models import Player


def check_name(name):
    isExist = True

    player = Player.query.filter_by(name=name).first()

    if not player:
        isExist = False

    return isExist


def addPlayer(data):

    message = 'Прости, но ты уже есть в списке игроков.\n\n'

    user_id = data['from_id']

    player = Player.query.filter_by(user_id=user_id).first()

    if not player:

        # получаем имя, так как оно последнее и без пробелов
        name = data['text'].split()[-1]
        
        if check_name(name):
            message = 'Такое имя уже есть в списке.\n\n'
            return message, ''

        date = datetime.datetime.today() + datetime.timedelta(hours=3)

        player = Player(user_id=user_id, name=name, date=date)
        db.session.add(player)
        db.session.commit()

        message = 'Я добавил тебя в таблицу.\n\n'

    players = Player.query.all()

    for player in players:
        message += player.name + " - " + player.date.strftime("%d/%m/%Y") + "\n"

    return message, ''


addPlayer_command = VKC.Command()
addPlayer_command.keys = ['Адик, добавь меня, я ']
addPlayer_command.desription = 'Добавляет игрока в таблицу'
addPlayer_command.proccess = addPlayer
