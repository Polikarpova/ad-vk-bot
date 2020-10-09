import app.vk_commands as VKC
from app.vkapi import get_list

def list(data):

    message = get_list()
    return message, ''


list_command = VKC.Command()
list_command.keys = ['Адик, покажи список', 'Адик, список']
list_command.desription = 'Выводит список игроков с датами'
list_command.proccess = list
