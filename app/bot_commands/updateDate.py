import app.vk_commands as VKC
import datetime
from app.extensions import db, scheduler, playerAlarmName
from app.models import Player
from app.vkapi import send_blame_message, get_list
from apscheduler.jobstores.base import JobLookupError


def check_blame_alarm(player, data):

    # находим в списке работ ту, что player_alarm+player_id
    jobName = playerAlarmName+str(player.user_id)

    try:
        scheduler.remove_job(job_id=jobName, jobstore='default')
    except JobLookupError:
        print("No job by the id of player_alarm202941722")

    run_date = player.date.replace(hour=15, minute=0, second=0, microsecond=0) + datetime.timedelta(weeks=3)

    scheduler.add_job(
        send_blame_message,
        'date',
        run_date=run_date,
        args=[data['group_id'], player.user_id, data['peer_id']],
        id=jobName,
        jobstore='default'
    )


def updateDate(data):

    user_id = data['from_id']

    player = Player.query.filter_by(user_id=user_id).first()

    if not player:
        message = 'Прости, но тебя нет в списке, напиши команду "Адик, добавь меня, я твой_никнейм" здесь или же через' \
                  ' личные сообщения, чтобы я мог зарегистрировать тебя. Для доступа к личным сообщениям, надо ' \
                  'вступить в мою группу https://vk.com/ApostolusDeiBot и написать мне лично :3.'
        return message, ''

    # игрок есть, значит обновляем
    date = datetime.datetime.today() + datetime.timedelta(hours=3)

    player.date = date
    db.session.commit()

    check_blame_alarm(player, data)

    message = 'Понято-принято от ' + player.name + '\n\n' + get_list()

    return message, ''


updateDate_command = VKC.Command()
updateDate_command.keys = ['+ ад', '+ад', '+ в ад', '+ ролка', '+ в ролку']
updateDate_command.desription = 'Обновляет дату последнего поста игрока'
updateDate_command.proccess = updateDate
