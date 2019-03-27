#coding:utf-8

import re
import sys
import threading
import optparse
import pyping

class MethodAddressError(Exception):
	def __init__(self, address_network=None):
		self.address_network = address_network

argument_service = optparse.OptionParser()
argument_service.add_option("-s", "--scan", dest="scan", help="Enter the IP.")
argument_service.add_option("-v", "--verbose", dest="verbose", help="It's mode verbose.")
(options, args) = argument_service.parse_args()

class CIDR(threading.Thread):
	def __init__(self, THREADS=35):
		threading.Thread.__init__(self)
		'''
			This function allows you to call
			the necessary options and arguments.
		'''
		self.THREADS = THREADS
		self.SCAN    = options.scan
		self.VERBOSE = options.verbose

		if(self.SCAN != None):
			self.SCAN  = re.findall('([0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3}\.[0-9]{0,3})', self.SCAN)
			if(not self.SCAN):
				raise MethodAddressError("Exception error address incorrect.")

	def __str__(self):
		'''
				The attack takes place here,
				so I create a __str__ function.
		'''
		self.SCAN = "".join(self.SCAN).split(".")
		self.SCAN = self.SCAN[0:3]
		self.SCAN = ".".join(self.SCAN)

		for number_text in range(1, 255):
			'''
				Created loop for generate random number in
				python and find the value in __str__.
			'''
			number_text       = str(number_text)
			operation_address = ((self.SCAN) + "." + number_text)

			service_icmp      = pyping.ping(operation_address)
			if(service_icmp.ret_code == 0):
				print("[*] Service found in network : %s" %(operation_address)) 
			else:
				print("[!] Service incorrect in network : %s" %(operation_address))

if __name__ == "__main__":
	Algorithm = CIDR()
	Algorithm.__str__()
