import os
import telegram
import subprocess

# Telegram bot token
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

# Create a Telegram bot using the `python-telegram-bot` library
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Handle command messages
def handle_command(message):
  # Parse the command and arguments from the message text
  text = message.text.split()
  command = text[0]
  args = text[1:]

  # Download a YouTube video
  if command == '/download':
    # Check if the user provided a YouTube URL
    if len(args) == 0:
      bot.send_message(chat_id=message.chat_id, text="Please provide a YouTube URL to download.")
      return

    # Use `yt-dlp` to download the YouTube video
    subprocess.run(["yt-dlp", args[0]])

    # Send a confirmation message to the user
    bot.send_message(chat_id=message.chat_id, text="Download started successfully!")

# Handle incoming messages
def handle_message(message):
  # Check if the message is a command
  if message.text.startswith('/'):
    handle_command(message)

# Start the bot
bot.start_polling()
