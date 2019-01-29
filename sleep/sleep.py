import time
import sys
import re

def sleeps():
   AlgorithmSleep = u"%s" %(sys.argv[1])
   if(AlgorithmSleep.isnumeric() == True):
      # Let's test if the argument is a number.
      AlgorithmSleep = int(AlgorithmSleep)
      time.sleep(AlgorithmSleep)

   elif(AlgorithmSleep.isnumeric() == False):
      print False

if __name__ == "__main__":
   sleeps()
