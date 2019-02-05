#coding:utf-8

import sys
import requests
import optparse

ModelPython = sys.version_info >= (3, 0)
# Grrrrrrrrrrrrrrrrrr
if(ModelPython):
  sys.exit('{!} Incorrect version of python.')

# This project allows to test latex vulnerability to have good thing.
# And to make a reverse shell for example.

class LatexIncorrectSerial(Exception):
  def __init__(self, LatexSerial=None):
    # If an error has occurred in prog.
    self.LatexSerial = LatexSerial
