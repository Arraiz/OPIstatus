from telegram.ext import Updater
from settings.bot_config import TOKEN_KEY,GROUP_ID,USERNAME
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import datetime

updater = Updater(token=TOKEN_KEY)
job = updater.job_queue
dispatcher = updater.dispatcher
t = datetime.time(16,17,00)

def start(bot, update):
    print(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def callback_minute(bot, job):
    bot.send_message(chat_id=GROUP_ID,
    text='One message every minute')

job_minute = job.run_daily(callback_minute, t)
#job_minute = job.run_daily(callback=callback_minute,datetime)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
    
