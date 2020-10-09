import app.vk_commands as VKC
from app.vk_commands import command_list


def botHelper(data):
    message = 'Вот какие есть команды:\n'

    for c in command_list:
        if c.keys[0].startswith('bot.'):
            message += c.keys[0].split()[0] + ' - ' + c.desription + '\n\n'

    return message, ''


botHelper_command = VKC.Command()
botHelper_command.keys = ['Bot.helper']
botHelper_command.desription = 'Информация о всех системных командах'
botHelper_command.proccess = botHelper
