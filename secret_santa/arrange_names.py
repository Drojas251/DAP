import numpy as np
import random 

# NAMES

class Person:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  
  def info(self):
    print(self.name)
    print(self.email)
    
  
p1 = Person("diego", "diego@email.com")
p2 = Person("ronni", "ronni@email.com")
p3 = Person("tito", "tito@email.com")
p4 = Person("marky","marky@email.com")
p5 = Person("jake", "jake@email.com")

  
names_list = [p1.name, p2.name, p3.name, p4.name, p5.name]
names_poll = [p1.name, p2.name, p3.name, p4.name, p5.name]
email_list = [p1.email, p2.email, p3.email, p4.email, p5.email]
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
i = 0
for nam in names_list:
	print('Player', nam)
	print('Your person is:', match[i])
	print('Send Email to ', email_list[i])
	print(' ' )
	
	i = i +1
	






