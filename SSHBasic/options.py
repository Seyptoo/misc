#coding:utf-8

from optparse import *

parser = OptionParser(add_help_option=False)
parser.add_option("-h", "--host", dest="host")
parser.add_option("-u", "--user", dest="user")
parser.add_option("-p", "--password", dest="password")
(options, args) = parser.parse_args()
HOST = options.host
USER = options.user
PASSWORD = options.password
