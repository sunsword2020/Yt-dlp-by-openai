# Import the required modules and classes
import os
import telegram
from telegram import ext
from telegram.ext import Updater, CommandHandler
import ytdl
from ytdl import Ytdl

# Get the Telegram bot token and yt-dlp path from the environment variables
token = os.environ['TELEGRAM_BOT_TOKEN']
ytdl_path = os.environ['YTDL_PATH']

# Create a Ytdl object with the specified path
ytdl = Ytdl(ytdl_path)

# Define the /download command handler
def download(update, context):
    # Get the URL of the video to download from the command arguments
    url = context.args[0]

    # Use the Ytdl object to download the video
    ytdl.download(url)

    # Send a message to the user to confirm that the download has started
    update.message.reply_text('Download started!')

# Create an Updater object with the bot token
updater = Updater(token, use_context=True)

# Get the dispatcher for the Updater object
dispatcher = updater.dispatcher

# Create a CommandHandler for the /download command
download_handler = CommandHandler('download', download)

# Add the CommandHandler to the dispatcher
dispatcher.add_handler(download_handler)

# Start the bot
updater.start_polling()

# Start the bot
bot.start_polling()
