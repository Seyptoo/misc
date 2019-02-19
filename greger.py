#coding:utf-8

import sys
import re
import thread
import options

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

class SSHLooper(thread.Threading):
	def __init__(self, threads=35):
		'''
			The pretty well-known parameters
			that I will put in the function.
		'''
		pass
