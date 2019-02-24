#coding:utf-8

import requests
import sys
import re
import color
import options
import time
import bs4 as BeautifulSoup

class RMUsernameNotFound(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

class RMErrorConnections(Exception):
	def __init__(self, ServerCondition=None):
		self.ServerCondition = ServerCondition

USER = options.PollersUser
LANG = options.PollersLang
CHAT = options.PollersChat
STAT = options.PollersStatus

def PollersUsers(WrapperService):
	'''
		I created a decorator to simplify
		things and speed things up easily
	'''
	if(USER == None):
		raise RMUsernameNotFound("No users typed.")
	return WrapperService

@PollersUsers
def PollersPoint():
	'''
		This function will consist
		of seeing the points of the user
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelSpan = re.findall('(<span>[0-9]+<\/span>)', ModelReqs)

	# He looks for the right value in the source of the page
	# The condition it tests if the user is existing.

	if(type(ModelSpan) == list and len(ModelSpan) != 0):
		BertModel = ModelSpan[0] # Take the first.
		BertModel = re.findall("[0-9]", BertModel)
		sys.exit("Point of "+USER+" : "+"".join(BertModel))
	else:
		raise RMUsernameNotFound("Username not found in DB.")

@PollersUsers
def PollersLangs():
	'''
		This function allows you to see
		the language of the user
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelServ = BeautifulSoup.BeautifulSoup(ModelReqs, "html5lib")

	# This function allows you to test the language and see the language of the user.
	# I used this time the Beautiful module to better manage things.

	try:
		RegexOnline = re.findall('(alt="[a-z]{0,2}")', ModelReqs)
		RegexOnline = "".join(RegexOnline).split('"')[1]
	except IndexError as e:
		if(not RegexOnline):
			sys.exit(e)

	# He will leave the program with this command.
	sys.exit("[+] Lang of the user : %s" %(RegexOnline))

@PollersUsers
def PollersChatBox():
	'''
		This function allows to
		see the chatbox of the user.
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelServ = BeautifulSoup.BeautifulSoup(ModelReqs, "html5lib")

	for ServiceLetter in re.findall('(<li>ChatBox&nbsp;:&nbsp;[0-9]{0,}<\/li>)', ModelReqs):
		ServiceLetter = re.findall('[0-9]', ServiceLetter)
		ServiceLetter = "".join(ServiceLetter)

	# He will leave the program with this command.
	sys.exit("[+] ChatBox of the user : %s" %(ServiceLetter))

@PollersUsers
def PollersStatus():
	'''
		This function allows to
		see the Status of the user.	
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelServ = BeautifulSoup.BeautifulSoup(ModelReqs, "html5lib")

	RegexStatus = re.findall('(<li>Statut|Status|estatus|&nbsp;:&nbsp;\w+.{0,}<\/li>)', ModelReqs)[1]
	if(type(RegexStatus) == unicode):
		RegexStatus = RegexStatus.replace("&nbsp;:&nbsp;", "")
		StatusRegex = RegexStatus.replace("</li>", "")

	# He will leave the program with this command.
	sys.exit("[+] Status of the user : %s" %(StatusRegex))

'''
	his part will correspond
	to the second part.
'''

@PollersUsers
def PollersAppScript():
	'''
			This function will allow us to see if the
			machines are hacked or not in the App-Script.
	'''
	ModelReqs = requests.get('https://www.root-me.org/%s?inc=score&lang=fr' %(USER)).text
	RegexApp = re.findall('(\/App-Script\/[A-Z0-9\-[a-z]+"\stitle="[0-9]{0,2}\s[A-Za-z]+">\s[ox])', ModelReqs)

	for PrefixPollers in RegexApp:
		PrefixPollers = PrefixPollers.split("/")
		PrefixPollers = PrefixPollers[2].split('"')

		# So we tested successfully and everything works fine.
		# There is no exception in this function for the moment so everything is fine.

		NameChallenge = PrefixPollers[0]
		OwnsChallenge = PrefixPollers[3]

		if("o" in OwnsChallenge):
			print(color.Y+"[+] %s : Owned" %(NameChallenge))
		elif("x" in OwnsChallenge):
			print(color.R+"[-] %s : Not Owned" %(NameChallenge))
