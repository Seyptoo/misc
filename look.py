#coding:utf-8

import requests
import sys
import re
import options

class RMUsernameNotFound(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

#options.ServicePollers()
USER = options.PollersUser
LANG = options.PollersLang

def PollersUsers(ValuePlease):
	'''
		I created a decorator to simplify
		things and speed things up easily
	'''
	if(type(USER) == str and USER == None):
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
	pass
