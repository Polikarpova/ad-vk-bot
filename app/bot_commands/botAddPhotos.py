import app.vk_commands as VKC
from app.extensions import db
from app.models import BlameMeme


def botAddPhotos(data):

    message = 'Добавлено'

    # вытаскиваем информацию из сообщения и добавляем
    str = data['text'].split('\n')
    length = len(str)

    for x in range(1, length):
        p = str[x].split(' ')

        photo_id = int(p[0])

        photo = BlameMeme(photo_id=photo_id)
        db.session.add(photo)
        db.session.commit()

    return message, ''


botAddPhotos_command = VKC.Command()
botAddPhotos_command.keys = ['Bot.addPhotos\n']
botAddPhotos_command.desription = 'Добавляет картинки для send_blame_message. Каждая картинка пишется с новой строки ' \
                                   'в следующем формате: photo_id'
botAddPhotos_command.proccess = botAddPhotos
