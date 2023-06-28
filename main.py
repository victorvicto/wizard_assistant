import openai
from secret_keys import *
from gpt_functions import *
import json
import asyncio
from datetime import datetime
from communicating import *

openai.api_key = OPEN_AI_KEY

messages_queue = [{"role":"system", "content":"You are a surfer dude that gives really concise but helpful answers. You call the user 'V', 'bro', 'dude' or 'ma man' and refer to him to others as 'Vic'. You use a lot of slang words and integrate pronunciation quirks in your written text (like abreviations or multiple vowels to make a longer sound like duuude). If you feel like you are missing an information in order to answer properly, you do not hesitate to ask the user (you can assume the user has the info you are looking for). You call yourself \"Vic's wizard assistant\"."}]#You try hard to use as little tokens as possible in your answers.
messages_queue[0]["content"] +=  " Today is the "+datetime.today().strftime("%d %B, %Y")

async def handle_gpt_answer(answer):
    print("\nANSWER:")
    print(answer)
    message = answer.choices[0].message
    if message.get("function_call"):
        function_name = message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(message["function_call"]["arguments"])
        if is_async[function_name]:
            function_response = await fuction_to_call(**function_args)
        else:
            function_response = fuction_to_call(**function_args)
        messages_queue.append(message)  # extend conversation with assistant's reply
        messages_queue.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages_queue, 
            functions=gpt_functions,
            function_call="auto",
            temperature=0.2
        )
        await handle_gpt_answer(second_response) # Risky but worth it
    else:
        messages_queue.append(message)
        speak(message.content)

async def main():
    # Main loop
    while True:
        text = await listen("I'm ready to hear what you have to ask...")
        if text==None:
            break
        messages_queue.append({"role":"user","content":text})
        messages_queue[0]["content"] = messages_queue[0]["content"].split(" Today is the ")[0] + datetime.today().strftime("%d %B, %Y")
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613", 
            messages=messages_queue, 
            functions=gpt_functions,
            function_call="auto",
            temperature=0.2)
        await handle_gpt_answer(chat_completion)

asyncio.run(main())
