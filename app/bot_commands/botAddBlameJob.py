import app.vk_commands as VKC
from app.models import Player
from app.extensions import scheduler, playerAlarmName
from datetime import timedelta
from app.vkapi import send_blame_message


def botAddBlameJob(data):

    message = 'Такого игрока не существует'

    user_id = int(data['text'].split()[1])

    player = Player.query.filter_by(user_id=user_id).first()

    if player:
        jobName = playerAlarmName + str(player.user_id)
        run_date = player.date.replace(hour=15, minute=0, second=0, microsecond=0) + timedelta(weeks=3)

        message = 'Для ' + player.name + ' добавлена напоминалка на ' +\
                  run_date.strftime('%d/%m/%Y, %H:%M:%S') + ' UTC+0'

        scheduler.add_job(
            send_blame_message,
            'date',
            run_date=run_date,
            args=[data['group_id'], player.user_id, 2000000003],
            id=jobName,
            jobstore='default'
        )

    return message, ''


botAddBlameJob_command = VKC.Command()
botAddBlameJob_command.keys = ['Bot.addBlameJob ']
botAddBlameJob_command.desription = 'Добавляет для игрока напоминалку о пропуске дедлайна. ' \
                                    'Принимает id игрока через пробел'
botAddBlameJob_command.proccess = botAddBlameJob
