#coding:utf-8

import requests
import sys
import re
import options
import bs4 as BeautifulSoup

class RMUsernameNotFound(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

USER = options.PollersUser
LANG = options.PollersLang

def PollersUsers(ValuePlease):
	'''
		I created a decorator to simplify
		things and speed things up easily
	'''
	if(USER == None):
		raise RMUsernameNotFound("No users typed.")
	return ValuePlease

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
		see the status of the user.
	'''
	ModelReqs = requests.get('https://www.root-me.org/'+USER).text
	ModelServ = BeautifulSoup.BeautifulSoup(ModelReqs, "html5lib")

	for ServiceLetter in re.findall('(<li>ChatBox&nbsp;:&nbsp;[0-9]{0,}<\/li>)', ModelReqs):
		ServiceLetter = re.findall('[0-9]', ServiceLetter)
		ServiceLetter = "".join(ServiceLetter)

	# He will leave the program with this command.
	sys.exit("[+] ChatBox of the user : %s" %(ServiceLetter))
