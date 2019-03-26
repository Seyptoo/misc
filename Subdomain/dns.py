#coding:utf-8

import sys
import tld
import requests
import optparse
import socket

class MethodRequestsError(Exception):
	def __init__(self, target_requests=None):
		self.target_requests = target_requests

def InvokeDomain(url_target):
	'''
		This function is used to test the
		functionality and parameters entered.
	'''
	if(requests.post(url_target).status_code == 200):	
		domain_get_tld = tld.get_fld(url_target)

	elif(requests.post(url_target).status_code != 200):
		raise MethodRequestsError("Requests status code is incorrect.")

	return domain_get_tld

def InvokeRequests():
	'''
		In this function I create
		options and requests sent
	'''
	ArgumentParse = optparse.OptionParser()
	ArgumentParse.add_option("-u", "--url", dest="url", help="It's URL")
	ArgumentParse.add_option("-w", "--wordlist", dest="wordlist", help="It's wordlist (list)")
	(options, args) = ArgumentParse.parse_args()

	url_selected      = options.url
	wordlist_selected = options.wordlist
 
	if(url_selected != None):
		url_selected = InvokeDomain(url_selected)

	if(wordlist_selected != None):
		with open(wordlist_selected, "r") as wordlist_selected:
			wordlist_selected = wordlist_selected.readlines()

		for texte_aline in wordlist_selected:
			'''
				I create a loop to
				perform the attack
			'''
			wordlist_selected = texte_aline.strip("\n")
			selected_dns      = wordlist_selected + "." + url_selected

			# I created a variable to gather the wordlist and the domain name
			# I create an exception to handle this.

			try:
				print("[*] Subdomain found : %s" %(select_dns))
			except socket.gaierror as exception_value:
				print(exception_value)

if __name__ == "__main__":
	InvokeRequests()
