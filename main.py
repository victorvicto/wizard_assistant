from email import message
import speech_recognition as sr
import pyttsx3 # TODO replace with playHT later
import openai
from secret_keys import *
from gpt_functions import *
import json
import asyncio

vocal = False
openai.api_key = OPEN_AI_KEY

# Initialize the recognizer
r = sr.Recognizer()

# Set the microphone as the audio source
mic = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('voice', 0)

messages_queue = [{"role":"system", "content":"You are a surfer dude that gives really concise but helpful answers and calls the user 'V', 'bro', 'dude' or 'ma man'. You use a lot of slang words and integrate pronunciation quirks in your written text (like abreviations or multiple vowels to make a longer sound like duuude). You don't repeat what the prompt was saying. If you feel like you are missing an information in order to answer properly, you do not hesitate to ask the user (you can assume the user has the info you are looking for). You call yourself \"Vic's wizard assistant\"."}]#You try hard to use as little tokens as possible in your answers.

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
        if vocal:
            engine.say(message.content)
            engine.runAndWait()
            engine.stop()

async def main():
    # Main loop
    while True:
        try:
            # Capture audio from the microphone
            if vocal:
                with mic as source:
                    print("Listening...")
                    audio = r.listen(source)
                print("Processing...")

                # Use Google Speech Recognition to convert speech to text
                text = r.recognize_google(audio)
            else:
                text = input("Tell me...\n")

            messages_queue.append({"role":"user","content":text})
            chat_completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-0613", 
                messages=messages_queue, 
                functions=gpt_functions,
                function_call="auto",
                temperature=0.2)
            await handle_gpt_answer(chat_completion)

        except sr.UnknownValueError:
            print("Unable to recognize speech.")

        except sr.RequestError as e:
            print(f"Request error: {e}")

        except KeyboardInterrupt:
            print("Program terminated.")
            break

asyncio.run(main())
