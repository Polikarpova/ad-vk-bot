import app.vk_commands as VKC
from app.vkapi import send_blame_message


def botTestBlameMessage(data):

    message = '...'

    send_blame_message(data['group_id'], data['from_id'], data['peer_id'])

    return message, ''


botTestBlameMessage_command = VKC.Command()
botTestBlameMessage_command.keys = ['Bot.testBlameMessage']
botTestBlameMessage_command.desription = 'Тестируем отправку сообщений'
botTestBlameMessage_command.proccess = botTestBlameMessage
