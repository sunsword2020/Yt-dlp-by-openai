import os
import telegram
from telegram import Bot
from telegram.utils.request import Request

def get_bot():
    # Default size from the library, 4 workers + 4 additional
    request = Request(con_pool_size=8)
    return Bot(token=os.getenv("TG_TOKEN"), request=request)
