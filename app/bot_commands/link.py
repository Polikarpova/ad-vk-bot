import app.vk_commands as VKC


def link(data):
    message = 'Вот ссылочка: http://makebelieve.starbb.ru/viewforum.php?id=28'
    return message, ''


link_command = VKC.Command()
link_command.keys = ['Адик, дай ссылку']
link_command.desription = 'Дает ссылку на форум'
link_command.proccess = link
