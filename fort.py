#coding:utf-8

import sys
import requests
import urllib

from bs4 import BeautifulSoup
from optparse import *

class dns_requests:
	def __init__(self, interface="tun0", target_ip="10.10.10.127"):
		'''
			I enter the parameters by default, and
			therefore to put the target and the interface
		'''
		self.target_ip = (target_ip)
		self.interface = (interface)
		self.target_ip = ("http://%s/select" %(self.target_ip))
