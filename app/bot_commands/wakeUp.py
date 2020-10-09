import app.vk_commands as VKC
import random

kaomodzi = ["(๑•́ωก̀๑).｡oO","( •́ωก̀)zzZ","(´っω=｀)", "(っ﹏-) .｡o", "(。‐ω⊂。)"]

def wakeUp(data):
    message = random.choice(kaomodzi)
    return message, ''


wakeUp_command = VKC.Command()
wakeUp_command.keys = ['Адик, подъем!', 'Адик, проснись!', 'Адик, подъем', 'Адик, проснись']
wakeUp_command.desription = 'Будит Адика'
wakeUp_command.proccess = wakeUp
