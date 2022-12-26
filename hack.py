import subprocess
from pyrogram import Client, filters
bot = Client("name", api_id="3030128", api_hash="cfc3885f5d2cbdbc5f10e6a643de2711",bot_token="2141733603:AAFmyuyeseVJZh3geZ83WJfT6yfizdpJagk")


chat_id = 12734305463
 list_png=[]
  
 for f in sorted(os.listdir(DIR_WITH_FILES)):
     if (str(f))[-3:] == "png":
        list_png.append(f)
         png_with_path=DIR_WITH_FILES+str(f)
         list_png_with_path.append(png_with_path)
    
 print(list_png)


bot.send_message(chat_id, text= "Downloading......" )
        prin = subprocess.run(["zippyshare-dl", link], capture_output=True, text=True).stdout.strip("\n")
        x=prin.split("\n")
        name = x[2].split(":")[1].strip(" ")
        size = x[3].split(":")[1]
        bot.send_message(chat_id, text= f"Download Success..... \nFile info \n\nFile Name = {name}\nSize = {size}" )
        bot.send_message(chat_id, text= "Uploading to telegram.....")
        x=prin.split("\n")
        bot.send_document(chat_id, document=name)
        subprocess.run(["rm", name])
    else:
        bot.send_message(chat_id, text="You are not allowed to use this bot")    
    print(prin)

bot.run()
