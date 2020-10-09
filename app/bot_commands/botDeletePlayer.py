import app.vk_commands as VKC
from app.extensions import db
from app.models import Player


def botDeletePlayer(data):

    name = data['text'][17:]

    player = Player.query.filter_by(name=name).first()

    if not player:
        message = 'Такого игрока нет в списке. Возможно он уже был удален'
        return message, ''

    # игрок есть, значит удаляем
    db.session.delete(player)
    db.session.commit()

    message = 'Игрок ' + player.name + ' был удален из списка игроков.\n\n'

    players = Player.query.all()

    for player in players:
        message += player.name + " - " + player.date.strftime("%d/%m/%Y") + "\n"

    return message, ''


botDeletePlayer_command = VKC.Command()
botDeletePlayer_command.keys = ['Bot.deletePlayer ']
botDeletePlayer_command.desription = 'Удаляет игрока по нику. Ник пишется через пробел после команды'
botDeletePlayer_command.proccess = botDeletePlayer
