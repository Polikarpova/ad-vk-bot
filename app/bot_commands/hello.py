import app.vk_commands as VKC


def hello(data):
    message = 'Привет!'
    return message, ''


hello_command = VKC.Command()
hello_command.keys = ['Привет бот', 'Привет, Бот', 'Привет Адик', 'Адик, привет', 'Адик привет']
hello_command.desription = 'Приветственное сообщение'
hello_command.proccess = hello
