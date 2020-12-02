import numpy as np
import smtplib


# Send email function 
def send_email(recipient, rec_email, name_pick):

	# email credentials
	sender_email = "secretsanta2020.510@gmail.com"
	password = "" # enter password
	
	#Set up server
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(sender_email,password)
	
	header = 'To:' + rec_email + '\n' + 'From: ' + sender_email + '\n' + 'Subject:Secret Santa!!! \n'
	
	msg = header + '\n Welcome to Secret Santa 2020!! \n\n' + '\n You Picked\n ' + name_pick + "\n $50 min, don't cheap out\n"
	server.sendmail(sender_email,rec_email, msg)
	print("Email has been sent to ", rec_email)
	print(" " )
	server.quit()
	
	
