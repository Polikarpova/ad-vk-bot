import app.vkapi as vkapi
import os
import importlib
from .vk_commands import command_list
from app.models import BlameMeme
from app.extensions import db, album_id


def load_commands():
    files = os.listdir('app/bot_commands')
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("app.bot_commands." + m[0:-3])


def get_command(data):
    text = data['text'].lower()
    command = None

    for c in command_list:
        tupleKeys = tuple(c.keys)
        if text.startswith(tupleKeys):
            command = c

    return command


def get_answer(command, data):
    return command.proccess(data)


def process_message(data, token):
    load_commands()
    peer_id = data['peer_id']

    command = get_command(data)

    # если команда есть
    if command:
        message, attachment = get_answer(command, data)
        vkapi.send_message(peer_id, token, message, attachment)


def upload_photo_in_database(data):

    if data['album_id'] == album_id:
        photo = BlameMeme(photo_id=data['id'])
        db.session.add(photo)
        db.session.commit()
    else:
        print('Это был загружен не мемасик')
