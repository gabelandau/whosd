"""
Telegram Bot to ask if people are D, or not.

Written by Gabe Landau. Find me on GitHub if you have questions!
"""

import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

# Enable logging.
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Handler for starting a poll.
def whosd(update, context):
  user_input = " ".join(context.args)
  update.message.reply_text("{} is D for {}".format(update.message.from_user.full_name, user_input))
  update.message.reply_text("Who else is D?")


# Handler for responding "Yes" to a poll.
def d(update, context):
  update.message.reply_text("{} is D.".format(update.message.from_user.full_name))


# Handler for responding "No" to a poll.
def notd(update, context):
  user_input = " ".join(context.args)
  update.message.reply_text("{} is not D. Reason: {}".format(update.message.from_user.full_name, user_input))


# Error handler
def error(update, context):
  logger.warning('Update "%s" caused error "%s"', update, context.error)


# Main
def main():
  load_dotenv()
  logger.info('Starting WhosD Bot, Version 0.0.1')
  logger.info('Running startup sequence...')
  updater = Updater(token=os.getenv('TOKEN'), use_context=True)
  dispatcher = updater.dispatcher

  dispatcher.add_handler(CommandHandler('whosd', whosd))
  dispatcher.add_handler(CommandHandler('d', d))
  dispatcher.add_handler(CommandHandler('notd', notd))

  dispatcher.add_error_handler(error)

  updater.start_polling()

  logger.info('Bot is ready and listening to commands...')


if __name__ == '__main__':
  main()