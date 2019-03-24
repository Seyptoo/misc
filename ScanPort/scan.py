#coding:utf-8

import sys
import socket
import re

class MethodAddressError(Exception):
	def __init__(self, target_address=None):
		self.target_address = target_address

try:
	InvokeAddressIP = sys.argv[1]
except IndexError as exception_model:
	sys.exit(exception_model)

def InvokeRequests(return_value):
	if not(re.findall('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})', InvokeAddressIP)):
		raise MethodAddressError("The IP address you entered is incorrect.")
	return return_value

@InvokeRequests
def InvokePortMods():
	socket_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	for number_port in range(0, 65535):
		try:
			socket_send.connect((InvokeAddressIP, number_port))
			print("[*] Port found : %s:%s" %(InvokeAddressIP, number_port))
		except socket.error as error_connection_socket:
			pass

if __name__ == "__main__":
	InvokePortMods()
		
