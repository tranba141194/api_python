from instabot import Bot
import os 

try:
    os.remove("config/nintran68_uuid_and_cookie.json")
except:
    pass
bot = Bot()
bot.login(username="nguyentranba141194@gmail.com", password="Tranba141194@@@")
users = bot.get_geotag_users(1720068614780997)
print(users)