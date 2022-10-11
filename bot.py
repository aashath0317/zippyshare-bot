import subprocess
from pyrogram import Client, filters
bot = Client("name", api_id="3030128", api_hash="cfc3885f5d2cbdbc5f10e6a643de2711",bot_token="2141733603:AAFmyuyeseVJZh3geZ83WJfT6yfizdpJagk")

@bot.on_message(filters.private)
def start(Client, message):
    chat_id = int(message.chat.id)
    link = message.text
    if chat_id == 1273430546:
        bot.send_message(chat_id, text= "Downloading......" )
        prin = subprocess.run(["zippyshare-dl", link], capture_output=True, text=True).stdout.strip("\n")
        bot.send_message(chat_id, text= "Download Success....." )
        bot.send_message(chat_id, text= "Uploading to telegram.....")
        x=prin.split("\n")
        name = x[2].split(":")[1].strip(" ")
        size = x[3].split(":")[1]
        bot.send_document(chat_id, document=name)
    else:
        bot.send_message(chat_id, text="You are not allowed to use this bot")    
    print(prin)

bot.run()
