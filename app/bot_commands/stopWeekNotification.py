import app.vk_commands as VKC
from app.extensions import scheduler, weeklyJobName
from apscheduler.jobstores.base import JobLookupError
import sys


def stopWeekNotification(data):

    message = 'Останавливаю недельные оповещения для этой беседы.'

    try:
        job_id = weeklyJobName + str(data['peer_id'])
        scheduler.remove_job(job_id=job_id, jobstore='default')
        scheduler.print_jobs(jobstore='default')
    except JobLookupError:
        print(sys.exc_info())

    return message, ''


stopWeekNotification_command = VKC.Command()
stopWeekNotification_command.keys = ['Адик, останови 7 дней']
stopWeekNotification_command.desription = 'Останавливает недельные оповещения'
stopWeekNotification_command.proccess = stopWeekNotification
