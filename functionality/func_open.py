import webbrowser
import subprocess
import json
import os
from voice.say import say

with open("database.json", "r") as f:
    database = json.load(f)

website = database["websites"]
apps = database["apps"]

def open_app(text,apps):
    for app in apps:
        if app["Name"].lower() in text.lower():
            say(f"Opening {app['Name']}")
            subprocess.Popen([
                "explorer.exe",
                f"shell:AppsFolder\\{app['AppID']}"
            ])
            return f"Opening {app['Name']}"
        
        say("Sorry, I could not find the app.")    

def open_website(text,website):
    for key in website.keys():
        if key.lower() in text.lower():
            say(f"Opening {key}")
            webbrowser.open(website[key])
            return f"Opening {key}"
        
        say("Sorry, I could not find the website.")    

def  open(text, apps, website):

    text = text.lower()

    if "open app" in text or "app" in text:
        return open_app(text, apps)
    elif "open website" in text or "website" in text:
        return open_website(text, website) 
              

      
            