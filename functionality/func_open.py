import webbrowser
import subprocess
import json
import os
from voice.say import say

database_path = os.path.join(os.path.dirname(__file__), "database.json")

with open(database_path, "r") as f:
    database = json.load(f)

website = database["websites"]
apps = database["apps"]

def open_app(text):
    try:
        for app in apps:
            if app["Name"].lower() in text.lower():
                say(f"Opening {app['Name']}")
                subprocess.Popen([
                    "explorer.exe",
                    f"shell:AppsFolder\\{app['AppID']}"
                ])
                return

        return say("Sorry, I could not find the app.")    

    except Exception as e:
        say(f"An error occurred while trying to open the app: {str(e)}")
        return        

def open_website(text):
    try:
        for key in website.keys():
            if key.lower() in text.lower():
                say(f"Opening {key}")
                webbrowser.open(website[key])
                return 

        return say("Sorry, I could not find the website.") 

    except Exception as e:
        say(f"An error occurred while trying to open the website: {str(e)}")
        return   

def  open(text):
    if "app" in text.lower():
        return open_app(text)
    elif "website" in text.lower():
        return open_website(text) 
    else:
        return say("Please specify whether you want to open an app or a website.")
              

      
            