from voice.say import say
from voice.listen import takecommand
from functionality import func_open

if __name__ == "__main__":
    print("JARVIS:")
    say("JARVIS is now online. How can I assist you?")

    while 1:
        print("Listening")
        text = takecommand()
        result = None

        if "exit" in text.lower():
            say("Goodbye!")
            break

        elif "open" in text.lower():
            result = func_open.open(text) 
        else:
            say("sorry, I couldn't find any results for your request.")

                    
