import vk_api
from vk_api.utils import get_random_id
from app.settings import token
from app.models import Player, BlameMeme
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from datetime import timedelta

session = vk_api.VkApi(token=token)
api = session.get_api()
deadlineOffset = timedelta(weeks=2)  # Двухнедельный дедлайн


def get_list():
    message = 'Список игроков и дат:\n'

    players = Player.query.order_by(desc(Player.date)).all()

    print(players)

    for player in players:
        deadlineDate = player.date + deadlineOffset
        message += player.name + " - последний пост: " + player.date.strftime("%d/%m/%Y") + ", дедлайн: " + \
                   deadlineDate.strftime('%d/%m/%Y') + "\n"

    return message


def get_random_photo(group_id):

    # вытащить имя фотки из бд
    photo = BlameMeme.query.order_by(func.random()).first()

    attachment = 'photo-' + str(group_id) + '_' + str(photo.photo_id)

    return attachment


def send_blame_message(group_id, player_id, peer_id):

    player = Player.query.filter_by(user_id=player_id).first()
    date = player.date+timedelta(weeks=2)
    message = '[id' + str(player_id) + '|' + player.name + '], твой дедлайн был неделю назад: ' + \
              date.strftime('%d/%m/%Y')

    attachment = get_random_photo(group_id)

    api.messages.send(
        access_token=token,
        peer_id=str(peer_id),
        message=message,
        random_id=get_random_id(),
        attachment=attachment
    )


def send_list(peer_id):

    message = get_list()

    api.messages.send(
        access_token=token,
        peer_id=str(peer_id),
        message=message,
        random_id=get_random_id(),
        attachment=""
    )


def send_message(peer_id, access_token, message, attachment=""):
    api.messages.send(
        access_token=access_token,
        peer_id=str(peer_id),
        message=message,
        random_id=get_random_id(),
        attachment=attachment
    )
