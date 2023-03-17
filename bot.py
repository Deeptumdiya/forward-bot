#    Copyright (c) 2021 Ayush
#    
#    This program is free software: you can redistribute it and/or modify  
#    it under the terms of the GNU General Public License as published by  
#    the Free Software Foundation, version 3.
# 
#    This program is distributed in the hope that it will be useful, but 
#    WITHOUT ANY WARRANTY; without even the implied warranty of 
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
#    General Public License for more details.
# 
#    License can be found in < https://github.com/Ayush7445/telegram-auto_forwarder/blob/main/License > .

from telethon import TelegramClient, events
from decouple import config
import logging
from telethon.sessions import StringSession

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

print("Starting...")

# Basics
APP_ID = 26723223
API_HASH = "dddfb6359abca7d422cf8d0b56d4c86b"
SESSION = "1BVtsOIgBu4cyzGZP6xJOejxh0pZ49m7AWDbPxRCT2ZlQ2ygA4xqDT_x8I5pnaQWi8JOyeTRBkG1K7uABarStwHGUMWOTyoIlh2BnQ92frDhnqeCdg3TGZeix5GKQIk_doWmX-nPDMIZ7sOOJ4hbhEwApqI6PObvyCOiBOkO85JbmHCGg9dD3KIGQ2rbrgm8a57Od75CXij9uh8VcmcPBFB7anp6XhVHdfVH1KwglmpXrx-ThQ1LYBOTwIKaf7BPKfA65yrnMPHRW-MIpP6xnjBE-znAM3mn3DvuDgqUpijotNaVtyKKV5NhDPFD_C4KQP8-AEjozcOi-TJoBmyMAvJOezVGf8j4="
FROM_ = "@rxce_colour_prediction_100"
TO_ = "@cooeofficials"
FROM = [i for i in FROM_.split()]
TO = [i for i in TO_.split()]

try:
    BotzHubUser = TelegramClient(StringSession(SESSION), APP_ID, API_HASH)
    BotzHubUser.start()
except Exception as ap:
    print(f"ERROR - {ap}")
    exit(1)

@BotzHubUser.on(events.NewMessage(incoming=True, chats=FROM))
async def sender_bH(event):
    message = "Want To Earn Daily 5k join this link --> https://cooe.in/promote/#/register?c=72FG1G0Y"
    for i in TO:
        try:
            if event.message.media:
                message = event.message
            else:
                codes = ["Y2B3F1FK", "7PR0A8WK"]
                for code in codes:
                    if code in event.message.message:
                        message = event.message.message.replace(code, "72FG1G0Y")
            await BotzHubUser.send_message(
                i,
                message
            )
        except Exception as e:
            print(e)

print("Bot has started.")
BotzHubUser.run_until_disconnected()
