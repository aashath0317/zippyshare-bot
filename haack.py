
import subprocess
import os
from pyrogram import Client, filters
import time
bot = Client("name", api_id="3030128", api_hash="cfc3885f5d2cbdbc5f10e6a643de2711",bot_token="1976201011:AAHMTReyFo2b81UD_nao3S41B-M602PFMxs")

filelist=os.listdir("/root/imgfiles")
for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".png")):
        filelist.remove(fichier)
loop = len(filelist)
looper = 0
@bot.on_message(filters.private)
def start(Client, message):
    while 1:
        filelist=os.listdir("/root/imgfiles")
        for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
            if not(fichier.endswith(".png")):
                filelist.remove(fichier)
        loop = len(filelist)
        looper = 0        
        chat_id = int(message.chat.id)
        while loop > looper:
            name = filelist[looper]
            looper = looper+1
            if chat_id == 1273430546:
                bot.send_document(chat_id, document=name)
                subprocess.run(["rm", name])
            else:
                bot.send_message(chat_id, text="You are not allowed to use this bot")   
        time.sleep(5)
bot.run()
