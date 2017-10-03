
import telepot
import youtube_dl as yt
import time
import os


path= "tmp/" #u can chouse unader folter per the 
yt_opts = {
    'outtmpl':'',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }]
}

def handle(msg):
    welcome="welcome!\nwith this bot u can downloder any yuotube video in mp3 format.\ncan u get me a youtube url and file name?"
    benvenuto = "ciao\n con questo bot puoi scaricare video da yt in formato mp3. iviami il link yt + il nome file\nNON SI ACCETTANO SPAZI!"
    content_type, chat_type, chat_id, = telepot.glance(msg)
    print (msg)

    with open('/home/makerfra/Documents/yt_bot/log/log.txt', 'w') as infile:
        infile.write(str(msg))

    if content_type == 'text':
        cmd = msg['text'].split()

        if cmd[0] == '/start':
            bot.sendMessage(chat_id, welcome)
            bot.sendMessage(chat_id, benvenuto)

        else:
            yt_opts['outtmpl'] = path + cmd[1]+".mp3"
            try:
                with yt.YoutubeDL(yt_opts) as ydl:
                    ydl.download([cmd[0]])
                    bot.sendAudio(chat_id, open(path + cmd[1]+".mp3", 'rb'))
                    print("send file...")
                    os.remove(path+cmd[1]+'.mp3')
                    print("file deleded...")
            except Exception as error:
                bot.sendMessage(chat_id, "error...")
                print(error)




token = "put here your token"
bot = telepot.Bot(token) 
bot.message_loop(handle)
print('I am listening ...')

while 1:
    time.sleep(10)


