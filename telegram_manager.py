import telegram
from secret_keys import *

wizard_bot = telegram.Bot(WIZARD_BOT_TELEGRAM_TOKEN)
async def send_message_to_friends(message):
    print("\nSENDING TELEGRAM MESSAGE:\n"+message+"\n\n")
    await wizard_bot.send_message(text=message, chat_id=WESSANT_CHAT_ID)
    return "{\"status\": \"sent\", \"message\":\""+message+"\"}"