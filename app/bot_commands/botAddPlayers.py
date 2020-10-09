import app.vk_commands as VKC
import datetime
from app.extensions import db
from app.models import Player


def botAddPlayers(data):

    message = 'Добавлено'

    # вытаскиваем информацию из сообщения и добавляем
    str = data['text'].split('\n')
    length = len(str)

    for x in range(1, length):
        p = str[x].split(' ')

        user_id = int(p[0])
        name = p[1]
        date = datetime.datetime.strptime(p[2], '%Y-%m-%d/%H:%M:%S')

        player = Player(user_id=user_id, name=name, date=date)
        db.session.add(player)
        db.session.commit()

    return message, ''


botAddPlayers_command = VKC.Command()
botAddPlayers_command.keys = ['Bot.addPlayers\n']
botAddPlayers_command.desription = 'Добавляет игроков в таблицу. Каждый игрок пишется с новой строки в следующем ' \
                                   'формате: user_id имя 1997-10-21/11:00:00'
botAddPlayers_command.proccess = botAddPlayers
