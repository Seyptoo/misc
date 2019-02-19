#coding:utf-8

import re
import threading
import options
import Queue

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
		threading.Thread.__init__(self)
		self.run()

		self.HOST = options.HOST
		self.USER = options.USER
		self.PASSWORD = options.PASSWORD
		self.THREADS = THREADS

	def run(self):
		'''
			This feature allows you to manage
			threads and all their functionality.
		'''
		q = Queue.Queue()
		with open(self.PASSWORD) as BertModel:
			for Queue_Reverse in BertModel:
				q.put(Queue_Reverse.rstrip("\n\r"))
			self.ExtensionModel(q)

		for i in range(int(self.THREADS)):
			worker = threading.Thread(name="ServicePollers", target=self.ExtensionModel, args=(i, q))
			worker.setDaemon(True)
			worker.start()
			worker.join(600)

		q.join()
