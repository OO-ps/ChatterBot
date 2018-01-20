import aiml
import os
import sqlite3
from Tkinter import *
import random
import server

#Retreving or Allocating Session ID
sessionId = random.randint(10000,1000000)
print ("Your Session ID is {}." .format(sessionId))

#Implementing the SQL Database
newpath = r'./sessions' 
if not os.path.exists(newpath):
    os.makedirs(newpath)
connection =sqlite3.connect('./sessions/{}.db'.format(sessionId))
cursor = connection.cursor()
sql_command = """ CREATE TABLE chat(submitted VARCHAR(100), output VARCHAR(100));"""
try: 
	cursor.execute(sql_command)
except sqlite3.OperationalError:
	print 'You have already had a session.'
connection.commit()

#Loading the AIML file.
kernel = aiml.Kernel()
kernel.learn('init.aiml')
kernel.respond("load aiml b")

#Chatting Begins
while True: 
	message = raw_input("Enter your message >> ")
	lowercase = message.lower()
	if lowercase.find('weather')>= 0:
		os.system('python server.py')
	else:
		response = kernel.respond(message)
		cursor.execute("INSERT INTO chat (submitted, output) VALUES (?, ?)", (message,response))
		connection.commit()
		print response