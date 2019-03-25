# -*- coding: utf-8 -*-

import sys
import requests

from optparse import *
from threading import Thread

parser = OptionParser()
parser.add_option("-u", "--url", dest="url", help="wordlist")
parser.add_option("-w", "--wordlist", dest="wordlist", help="wordlist")
(options, args) = parser.parse_args()

def InvokeRequests():
	with  open(options.wordlist, "r") as ExtensionModel:
		wordlist_append = ExtensionModel.readlines()

	for property_line in wordlist_append:
		property_line = property_line.strip("\n")
		if(requests.post(options.url + property_line).status_code == 200):
			print("[*] Fuzzing directory : %s" %(property_line))

if __name__ == "__main__":
	InvokeRequests()
