import subprocess
from pyrogram import Client, filters
bot = Client("name", api_id="", api_hash="",bot_token="")

@bot.on_message(filters.private)
def start(Client, message):
    chat_id = int(message.chat.id)
    if chat_id == 
        bot.send_message(chat_id, text= "Downloading......" )
        prin = subprocess.run(["zippyshare-dl","https://www62.zippyshare.com/v/ZMHll2Qa/file.html"], capture_output=True, text=True).stdout.strip("\n")
        bot.send_message(chat_id, text= "Download Success....." )
        bot.send_message(chat_id, text=prin)
    else
        bot.send_message(chat_id, text="You are not allowed to use this bot")    
    print(prin)

bot.run()
