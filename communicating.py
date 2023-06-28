import pyttsx3 # TODO replace with playHT later
import speech_recognition as sr

VOCAL_SPEECH = False
VOCAL_LISTEN = False

engine = pyttsx3.init()
engine.setProperty('voice', 0)

r = sr.Recognizer()
mic = sr.Microphone()

async def confirm(message):
    speak(message)
    res = await listen("\nconfirm? (yes/no)")
    if res==None:
        speak("An error happened")
        return False
    if res.lower().strip()=="yes":
        return True
    return False

def speak(message):
    if VOCAL_SPEECH:
        engine.say(message.content)
        engine.runAndWait()
        engine.stop()
    else:
        print(message)
        print()

async def listen(message):
    speak(message)
    while True:
        if VOCAL_LISTEN:
            try:
                with mic as source:
                    print("Listening...")
                    audio = r.listen(source)
                print("Processing...")

                # Use Google Speech Recognition to convert speech to text
                text = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Unable to recognize speech.")

            except sr.RequestError as e:
                print(f"Request error: {e}")

            except KeyboardInterrupt:
                print("Program terminated.")
                break
        else:
            text = input()
        if len(text)>0:
            return text
    return None