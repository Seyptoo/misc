#coding:utf-8

import sys
import hmac
import base64

from Crypto.Cipher import DES
from hashlib import sha1

class ARK_OBJ(object):
	def __init__(self, block_size=8):
		'''
			This function will
			handle the arguments in function __init__().
		'''
		try:
			self.args       = sys.argv[1]
			self.args_      = sys.argv[2]
		except IndexError as output_file:
			sys.exit("Usage: python %s <payload-file> <output>" %(sys.argv[0]))

		self.block_size = block_size

	def pad(self, plain):
		'''
			This function will handle the
			encryption of the data in function __pad()__.
		'''
		return plain + ((self.block_size - len(plain) % self.block_size) * chr(self.block_size - len(plain) % self.block_size)).encode('ascii')

	def reverse_dt(self):
		'''
			This function will allow us
			to manipulate with the hashes.
		'''
		with open(self.args, "rb") as self.serial:
			self.payload = self.serial.read()

		self.key          = b'JsF9876-'
		self.payload      = self.pad(self.payload)

		# This part we will encrypted in
		# hmac and then put it in base64 __reverse_dt()__.

		self.convert_des  = DES.new(self.key, DES.MODE_ECB)
		self.text_data    = self.convert_des.encrypt(self.payload)
		self.convert_hmac = hmac.new(self.key, self.text_data, sha1).digest()

		with open(self.args_, "wb") as write_file:
			write_file.write(base64.b64encode(self.text_data + self.convert_hmac))

if __name__ == "__main__":
	q = ARK_OBJ()
	q.reverse_dt()
