import logging, re, random
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from time import sleep

TOKEN = ""

#enable logging
logging.basicConfig(
    filename='logfile.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context):
    '''
    This simple bot send random line from text file every 120 seconds
    '''
    user = update.effective_user
    update.message.reply_text('Hello!')
    while True:
        text = choose_text()
        update.message.reply_text(text)
        sleep(120)
    
def choose_text():
    lines = open('text.txt').read().splitlines()
    myline =random.choice(lines)
    return myline


def helpCommand(update: Update, context):
    update.message.reply_text('HELP_MESSAGE_HERE')

def main():
    updater = Updater(TOKEN, use_context=True)

    # Create handler dispatcher
    dp = updater.dispatcher

		
	# Add command handlers 
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpCommand))
		
	# start bot
    updater.start_polling()

	# stop bot via ctrl+c
    updater.idle()


if __name__ == '__main__':
    main()

