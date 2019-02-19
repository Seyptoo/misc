#coding:utf-8

import re
import threading
import options
import Queue

class SSHArgumentNotFound(Exception):
	def __init__(self, ArgumentExcepts=None):
		self.ArgumentExcepts = ArgumentExcepts

class SSHIncorrectAddress(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

def OutputArgument():
	'''
		This function will test the
		necessary variables and arguments.
	'''
	ArgsHOST = re.findall(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", options.HOST)
	if(type(ArgsHOST) == list and len(ArgsHOST) == 0):
		raise SSHIncorrectAddress("Incorrect Address SSH sorry.")

	# We already start the mistakes to do that.
	# I create an express function for that.

class SSHLooper(threading.Thread):
	def __init__(self, THREADS=35):
		'''
			The pretty well-known parameters
			that I will put in the function.
		'''
		self.HOST = options.HOST
		self.WORDLIST = options.WORDLIST
		self.THREADS = THREADS
