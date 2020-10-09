import app.vk_commands as VKC
from app.extensions import scheduler


def botAllJobs(data):

    scheduler.print_jobs(jobstore='default')
    message = str(scheduler.get_jobs(jobstore='default')) + '\n\nБольше информации смотри в логах:' \
                                                           ' https://dashboard.heroku.com/apps/ad-vk-bot/logs'

    return message, ''


botAllJobs_command = VKC.Command()
botAllJobs_command.keys = ['Bot.sheduler.all_job']
botAllJobs_command.desription = 'Выводит в логи и в сообщения все оповещения (в логах подробнее)'
botAllJobs_command.proccess = botAllJobs
