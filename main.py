import json
from voice.say import say
from voice.listen import takecommand
import functionality.func_open as func_open


if __name__ == "__main__":
    print("JARVIS:")
    say("JARVIS is now online. How can I assist you?")

    while 1:
        print("Listening")
        text = takecommand()
        result = None

        if "exit" in text or "quit" in text:
            say("Goodbye!")
            break

        elif "open" in text:
            result = func_open.open(text, apps, website) 

        say(f"result: {result}")    

                    
