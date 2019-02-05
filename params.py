#coding:utf-8

import sys
import requests

from optparse import *
from modules import options

# This project allows to test latex vulnerability to have good thing.
# And to make a reverse shell for example.

class LatexIncorrectSerial(Exception):
	def __init__(self, LatexSerial=None):
		'''
		I create a specific function
		for an exception for a reason.
		'''
		self.LatexSerial = LatexSerial

class LatexArgumentation:
	def __init__(self):
		'''
			Creating arguments to
			do something cool.
		'''
		self.URL = options.ArgumentURL
		self.POST = options.ArgumentPOST

	def StringLT(self):
		'''
			The attack takes place
			at this precise function.
		'''
		if(self.URL.startswith(("http://", "https://")) == False):
			raise LatexIncorrectSerial("URL crashed !")

if __name__ == "__main__":
	Argument = LatexArgumentation()
	Argument.StringLT()
