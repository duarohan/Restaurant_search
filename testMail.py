import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import Config

class EmailClass:
	
	def __init__(self):
		self.config = Config().getConfig()
	
	def sendmail(self,recepientEmail):
		sender_address = self.config['senders_email']
		sender_pass = self.config['senders_password']
		receiver_address = recepientEmail
		mail_content = 'Hello, This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library. Thank You'
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Sample Program'   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		print('text',text)
		print('message',message)
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		print('Mail Sent')
	

def main():
	email = EmailClass()
	email.sendmail('abc@xyz.com')

if __name__ == "__main__":
    main()   
