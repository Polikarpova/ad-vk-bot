import app.vk_commands as VKC

def info(data):
    message = 'Привет! Меня зовут Адик и я бот-менеджер, который будет помогать вам следить за дедлайнами!' \
              '\n Ты можешь писать мне команды как в беседе, в которую меня добавили, так и через личные сообщения,' \
              ' для этого вступи в мою группу: https://vk.com/ApostolusDeiBot и напиши мне сообщение через неё.' \
              '\n 1. Напиши мне "Адик, помоги" и появится информационное сообщение обо ' \
              'всех моих командах. Сами команды не чувствительны к регистру, но свой никнейм надо писать с учетом ' \
              'регистра. Анакои и анакои для меня - это два разных имени' \
              '\n 2. Напиши мне "Адик, добавь меня, я твой_никнейм", чтобы я мог добавить тебя в список. Имя должно ' \
              'быть без пробелов!' \
              '\n 3. Напиши "+ ад" и я обновлю дату твоего последнего поста на текущую.' \
              '\n 4. Напиши мне "Адик, список" и я отправлю вам список игроков и дат их последнего поста.' \
              '\n 5. Напиши мне "Адик, дай ссылку" и я отправлю вам ссылку на форум ролевой.' \
              '\n 6. Напиши мне "Адик, запусти 7 дней день время", где день записывается двумя буквами (ПН, ВТ, СР и ' \
              'т.д.), а время - это часы:минуты, например 19:30. Эта команда запускает недельную рассылку игроков и ' \
              'последней даты их поста в то время и день недели, которое было указано в команде.' \
              '\n 7. Напиши мне "Адик, останови 7 дней" и я остановлю недельную рассылку списка игроков.' \
              '\n 8. Напиши мне "Адик, подъем" во время сонного режима (с 00:00 до 12:00 по мск), перед тем как ' \
              'отдать мне команду.'

    return message, ''


info_command = VKC.Command()
info_command.keys = ['Адик, помоги']
info_command.desription = 'Информация'
info_command.proccess = info