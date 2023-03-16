#!/bin/python3
# This is the NetProgrammer v2 Classes file by Rick Allen

import sys
import getpass
import os
import time
import subprocess
import paramiko
import re
import json


class File_Handler:
    def Open_File(self,file_name):
        if file_name.endswith('.json'):
            with open(os.path.join(sys.path[0], file_name)) as json_file:
                json_parse = json.load(json_file)
                return json_parse
            json_file.closed
        else:
            print('File type not supported')

class Login:
    def __init__(self):
        self.username = ''
        self.password = ''

    def cred_harvest(self):
        self.username = input('Username: ')
        self.password = getpass.getpass()

class The_Great_Connector:
    def send_command(self,username,password,host,command):
        remote = paramiko.SSHClient()
        remote.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # for h in mn2.selected:
        #     print(h.values()['name'])
        try:
            remote.connect(host, username = username, password = password, look_for_keys = False, allow_agent = False)
            print('Connection Sucessfull...')
            remote_conn = remote.invoke_shell()
            # remote_conn.send('en\n')
            # remote_conn.send(password + '\n')
            # remote_conn.send('terminal pager 0\n')
            remote_conn.send('no page\n')
            output = remote_conn.recv(1000)
            remote_conn.send('\n')
            remote_conn.send(command + '\n')
            time.sleep(2)
            output = remote_conn.recv(9999)
            # os.system('clear')
            print('---------------------------------------- Begin ' + str(host) + ' ----------------------------------------')
            print(output.decode('utf-8'))
            print('----------------------------------------- End ' + str(host) + ' -----------------------------------------')
        except:
            print('\nLooks like authentication failed cheif...')
            time.sleep(1)
            print('you should try to login again')
            time.sleep(2)
    # input('\nPress Enter to continue...')
