import app.vk_commands as VKC
from app.extensions import scheduler, weeklyJobName
from app.vkapi import send_list

daysDict = {
    'ПН': 'mon',
    'ВТ': 'tue',
    'СР': 'wed',
    'ЧТ': 'thu',
    'ПТ': 'fri',
    'СБ': 'sat',
    'ВС': 'sun'
}


def startWeekNotification(data):

    peer_id = data['peer_id']

    jobName = weeklyJobName+str(peer_id)

    job = scheduler.get_job(job_id=jobName, jobstore='default')

    if job is not None:
        message = 'Для этой беседы оповещение уже создано. Если вы хотите отменить существующее, то напишите ' \
                  '"Адик, останови 7 дней", чтобы запустить новое оповещение.'
        return message, ''

    text = data['text'].split(' ')

    day = text[-2]
    hour = int(text[-1].split(':')[0]) - 3

    message = 'Запускаю недельные оповещения. Дата оповещения: ' + day + ' в ' + text[-1] + '.'

    if hour < 0:
        hour = 24 + hour

        dayList = list(daysDict.keys())
        day = dayList[dayList.index(day)-1]

    minute = int(text[-1].split(':')[1])

    job_id = weeklyJobName + str(peer_id)

    scheduler.add_job(
        send_list,
        'cron',
        day_of_week=daysDict.get(day),
        hour=hour,
        minute=minute,
        args=[peer_id],
        id=job_id,
        jobstore='default'
    )
    scheduler.print_jobs(jobstore='default')

    return message, ''


startWeekNotification_command = VKC.Command()
startWeekNotification_command.keys = ['Адик, запусти 7 дней ']
startWeekNotification_command.desription = 'Выводит список игроков каждые семь дней'
startWeekNotification_command.proccess = startWeekNotification
