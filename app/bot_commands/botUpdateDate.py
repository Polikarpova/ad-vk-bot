import app.vk_commands as VKC
import datetime
from app.extensions import db
from app.models import Player


def botUpdateDate(data):

    text = data['text'].split(' ')

    name = text[1]
    date = datetime.datetime.strptime(text[2], '%d/%m/%Y')

    player = Player.query.filter_by(name=name).first()

    if not player:
        message = 'Такого игрока нет'
        return message, ''

    # игрок есть, значит обновляем
    player.date = date
    db.session.commit()

    message = 'Обновлена дата последнего поста игрока ' + player.name + '\n\n'

    players = Player.query.all()

    for player in players:
        message += player.name + " - " + player.date.strftime("%d/%m/%Y") + "\n"

    return message, ''


botUpdateDate_command = VKC.Command()
botUpdateDate_command.keys = ['Bot.updateDate ']
botUpdateDate_command.desription = 'Обновляет дату последнего поста по нику. Ник пишется через пробел после команды.' \
                                   ' После ника пишется дата в формате 21/10/2020.'
botUpdateDate_command.proccess = botUpdateDate
