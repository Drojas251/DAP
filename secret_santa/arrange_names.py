import numpy as np
import random 
from utils_DAP import send_email

# NAMES

class Person:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  
  def info(self):
    print(self.name)
    print(self.email)
  
    	
  	
p1 = Person("Diego", "drojas@ucdavis.edu")
p2 = Person("Ronni", "ronnigonzo@gmail.com")
p3 = Person("Luna", "Edwardluna44@gmail.com")
p4 = Person("Marky","marcus.marquez@sjsu.edu")
p5 = Person("Jake", "jakeruiz7@yahoo.com")
p6 = Person("Isa", "isamont510@gmail.com")
p7 = Person("Chris", "chriscar777@att.net")
p8 = Person("Nava", "Navae25@yahoo.com")

  
names_list = [p1.name, p2.name, p3.name, p4.name, p5.name,p6.name ,p7.name ,p8.name]
names_poll = [p1.name, p2.name, p3.name, p4.name, p5.name,p6.name ,p7.name ,p8.name]
email_list = [p1.email, p2.email, p3.email, p4.email, p5.email,p6.email, p7.email, p8.email]
match = []



for name in names_list:
	true = 1
	num = random.randint(0,len(names_poll)-1)
	while true ==1:

		if name == names_poll[num]:
			num = random.randint(0,len(names_poll)-1)

		else:
			match.append(names_poll[num])
			names_poll.remove(names_poll[num])
			true = 0

#i = 0
#for nam in names_list:
#	print('Player', nam)
#	print('Your person is:', match[i])
#	print('Send Email to ', email_list[i])
#	print(' ' )
	
#	i = i +1
i =0
for names in names_list:
	send_email(names, email_list[i], match[i])
	i = i +1
	






