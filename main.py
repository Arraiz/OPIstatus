from telegram.ext import Updater
from settings.bot_config import TOKEN_KEY,GROUP_ID,USERNAME,TIME,COMMANDS
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import datetime
import os

updater = Updater(token=TOKEN_KEY)
job = updater.job_queue
dispatcher = updater.dispatcher


def status(bot,update):
    if(update.message.chat_id == GROUP_ID):
        #uptime
        uptime=os.popen(COMMANDS['UPTIME']).read()

        #disk space
        disk_space = os.popen(COMMANDS['DISK']).read()
        #logs in day

        response = "%s\n%s"%(uptime,disk_space)
        bot.send_message(chat_id=update.message.chat_id, text=response)


def callback_minute(bot, job):
    bot.send_message(chat_id=GROUP_ID,
    text='OPI is UP')

def main():
    job.run_daily(callback_minute, TIME)
    status_handler = CommandHandler('status', status)
    dispatcher.add_handler(status_handler)
    updater.start_polling()


if __name__ == "__main__":
    main()