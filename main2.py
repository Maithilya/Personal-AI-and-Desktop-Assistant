import speech_recognition as sr
import os
import webbrowser
import google.generativeai as genai
#from config import apikey
import datetime
import random
#import numpy as np
import win32com.client


def pyttsx3(text):
    os.system(f'pyttsx3 "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold= 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error occured. Sorry from Jarvis"
if __name__ == '__main__':
    print('Pycharm')
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak("Hello I am Rajju")
    while True:
        print("listening...")
        query= takeCommand()
        sites=[["youtube","https://youtube.com"],["wikipedia","https://www.wikipedia.com"],["Google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.speak(f"Opening {site[0]} maleek...")
                webbrowser.open(site[1])
        #speaker.speak(query)
        paths=[["23","C:/Users/maith/OneDrive/Desktop/23"],["Weekly Reports","C:/Users/maith/OneDrive/Desktop/Weekly Reports"],["hj","C:/Users/maith/OneDrive/Desktop/hj"],["DO","C:/Users/maith/OneDrive/Desktop/DO"],["internship","C:/Users/maith/OneDrive/Desktop/internship"],["final year project","C:/Users/maith/OneDrive/Desktop/final year project"],["sign language","C:/Users/maith/OneDrive/Desktop/sign language"],["trio","C:/Users/maith/OneDrive/Desktop/trio"],["portfolio wesite","C:/Users/maith/OneDrive/Desktop/portfolio wesite"],["girls reel","C:/Users/maith/OneDrive/Desktop/girls reel"]]
        for path in paths:
            if f"Open {path[0]}".lower() in query.lower():
                speaker.speak(f"Opening folder {path[0]} from desktop maleek...")
                os.startfile(path[1])

        if "open memory" in query:
            memoryPath= "C:/Users/maith/OneDrive/Desktop/23"
            os.startfile(memoryPath)

        if "the time" in query:
            #memoryPath= "/Users/HP/OneDrive/Pictures/20230823_011905.jpg"
            strfTime = datetime.datetime.now().strftime(" %I:%M: %p %d %m %Y")
            speaker.speak(f"The time is {strfTime}")

        if "open camera" in query:
            cameraPath= "start microsoft.windows.camera:"
            os.system(cameraPath)
        ai=()
        if f"Raju".lower() in query.lower():
            from config2 import apikey

            os.environ["GOOGLE_API_KEY"] = apikey
            import google.generativeai as genai

            genai.configure(api_key=os.getenv(apikey))

            # Create the model
            generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }

            model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=generation_config,
                system_instruction="your name is rajj u not a text base ai  be funny in ever line and i am your maaleek stop saying hay at the begigning of the responce, you have to be humorous and give specfic answes to me, but keep it short and sweet dont use emoji,dont reffer jarvis in any conversetion ,dont anwswer more than needed,try to answer in 1 line,dont respond if there is nothing in command,dont reffer jarvis in conversetion ,stop saying hey,remember that when ever i ask you to to do a task that you cant perform just reply i tried my best",
            )

            history = []

            while True:

                chat_session = model.start_chat(
                    history=history
                )
                response = chat_session.send_message(query)
                model_response = response.text
                speaker.speak(f'Bot: {model_response}')
                history.append({"role": "user", "parts": [query]})
                history.append({"role": "model", "parts": [model_response]})
                speaker.speak("")
                print("listening...")
                query = takeCommand()
                sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                         ["Google", "https://www.google.com"]]
                for site in sites:
                    if f"Open {site[0]}".lower() in query.lower():
                        speaker.speak(f"Opening {site[0]} maleek...")
                        webbrowser.open(site[1])
                # speaker.speak(query)
                paths = [["23", "C:/Users/maith/OneDrive/Desktop/23"],
                         ["Weekly Reports", "C:/Users/maith/OneDrive/Desktop/Weekly Reports"],
                         ["hj", "C:/Users/maith/OneDrive/Desktop/hj"], ["DO", "C:/Users/maith/OneDrive/Desktop/DO"],
                         ["internship", "C:/Users/maith/OneDrive/Desktop/internship"],
                         ["final year project", "C:/Users/maith/OneDrive/Desktop/final year project"],
                         ["sign language", "C:/Users/maith/OneDrive/Desktop/sign language"],
                         ["trio", "C:/Users/maith/OneDrive/Desktop/trio"],
                         ["portfolio wesite", "C:/Users/maith/OneDrive/Desktop/portfolio wesite"],
                         ["girls reel", "C:/Users/maith/OneDrive/Desktop/girls reel"]]
                for path in paths:
                    if f"Open {path[0]}".lower() in query.lower():
                        speaker.speak(f"Opening folder {path[0]} from desktop maleek...")
                        os.startfile(path[1])

                if "open memory" in query:
                    memoryPath = "C:/Users/maith/OneDrive/Desktop/23"
                    os.startfile(memoryPath)

                if "the time" in query:
                    # memoryPath= "/Users/HP/OneDrive/Pictures/20230823_011905.jpg"
                    strfTime = datetime.datetime.now().strftime(" %I:%M: %p %d %m %Y")
                    speaker.speak(f"The time is {strfTime}")

                if "open camera" in query:
                    cameraPath = "start microsoft.windows.camera:"
                    os.system(cameraPath)
                ai = ()



        #files=[["tcs"],["ai"],["apikey"]]
        #for file in files:
         #   if f"Open {file[0]} from internship".lower() in query.lower():
          #      speaker.speak(f"Opening folder {file[0]} from desktop maleek...")
           #     os.startfile("C:/Users/maith/OneDrive/Desktop/internship/",file[0])
        if "open memory" in query:
            memoryPath= "C:/Users/maith/OneDrive/Desktop/23"
            os.startfile(memoryPath)



