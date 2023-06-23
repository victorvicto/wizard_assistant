import telegram
from secret_keys import *
import asyncio

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

wizard_bot = telegram.Bot(WIZARD_BOT_TELEGRAM_TOKEN)
async def send_message_to_friends(message):
    print("\nSENDING TELEGRAM MESSAGE:\n"+message+"\n\n")
    await wizard_bot.send_message(text=message, chat_id=WESSANT_CHAT_ID)
    return "{\"status\": \"sent\", \"message\":\""+message+"\"}"

gpt_functions = [
    {
        "name": "send_message_to_friends",
        "description": "Sends a message to the user's friends via a group chat. This goup chat's members are the user and his friends. The message will look like it has been sent by a bot called \"Vic's wizzard assistant\".",
        "parameters": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string",
                    "description": "The message that should be sent to the group chat.",
                }
            },
            "required": ["message"],
        },
    }
]

available_functions = {
    "send_message_to_friends": send_message_to_friends
}

