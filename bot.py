# Import the required modules and classes
import os
import subprocess
import telegram
import telegram.ext
import telegram.ext.jobqueue
from telegram.vendor.ptb_urllib3.urllib3.poolmanager import PoolManager
from utils import get_bot

# Telegram bot token
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Create a job queue
job_queue = telegram.ext.jobqueue.JobQueue()

# Create a Telegram bot using the `python-telegram-bot` library
bot = get_bot()

# Create an Updater object
updater = telegram.ext.Updater(bot=bot)

# Create a Dispatcher object
dispatcher = telegram.ext.Dispatcher(bot, update_queue=updater.update_queue)

# Handle command messages
def handle_command(update: telegram.Update, context: telegram.ext.CallbackContext, job_queue):
  # Parse the command and arguments from the message text
  text = update.message.text.split()
  command = text[0]
  args = text[1:]

  # Download a YouTube video
  if command == '/download':
    # Check if the user provided a YouTube URL
    if len(args) == 0:
      context.bot.send_message(chat_id=update.message.chat_id, text="Please provide a YouTube URL to download.")
      return

    # Use `yt-dlp` to download the YouTube video
    subprocess.run(["yt-dlp", context.args[0]])

    # Send a confirmation message to the user
    context.bot.send_message(chat_id=update.message.chat_id, text="Download started successfully!")

    # Register the handle_command() function as a CommandHandler
dispatcher.add_handler(telegram.ext.CommandHandler('download', handle_command))

# Start the Dispatcher
dispatcher.start()
