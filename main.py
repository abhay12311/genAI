import speech_recognition as sr
import pyttsx3
import webbrowser
import json

with open("databse.json", "r") as f:
    website = json.load(f)


# print("Welcome to the Speech Recognition Program!")

# import win32com.client as win32
# speaker = win32.Dispatch("SAPI.SpVoice")

# while True:
#     print("Enter the word you want to speak (or type 'exit' to quit):")
#     s = input()
#     if (s.lower() == 'exit'):
#             break;
#     speaker.Speak(s)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
        return query    

    except Exception as e:
        print("Sorry, I did not catch that,")
        return ""

# if __name__ == "__main__":
#     print("JARVIS:")
#     say("JARVIS is now online. How can I assist you?")

#     while 1:
#         print("Listening")
#         text = takecommand()
#         # say(text)
#         # print("you said: "+ text)

#         if "exit" in text or "quit" in text:
#             say("Goodbye!")
#             break

#         if "open youtube".lower() in text.lower():
#             say("Opening YouTube")
#             webbrowser.open("https://www.youtube.com")
#             break


if __name__ == "__main__":
    print("JARVIS:")
    say("JARVIS is now online. How can I assist you?")

    while 1:
        print("Listening")
        text = takecommand()

        if "exit" in text or "quit" in text:
            say("Goodbye!")
            break

        for key in website.keys():
            if key in text.lower():
                say(f"Opening {key}")
                webbrowser.open(website[key])   
