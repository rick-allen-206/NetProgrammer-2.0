#!/bin/python3

# This is the NetProgrammer v2 Script by Rick Allen

import NetProgrammer_Classes
import sys
import os
import time

lg1 = NetProgrammer_Classes.Login()
fh1 = NetProgrammer_Classes.File_Handler()
gc1 = NetProgrammer_Classes.The_Great_Connector()
Menu_Dict = fh1.Open_File('HostsList.json')['Menu_List_Items']
Hosts_Dict = fh1.Open_File('HostsList.json')['Hosts']
selected_hosts = []

def menu():
    # ------------------- #
    # Function Settings
    # --------------------#
    listofkeys = list(Menu_Dict.keys())
    choice = ''
    os.system('clear')

    # ------------------- #
    # print menu function
    # --------------------#
    print('************ MAIN MENU **************' + '\n')
    if lg1.username != '': #---------------------------------------------------- If username is defined, welcom user
        print('Welcome ' + lg1.username + '\n')
    print(selected_hosts)
    print()
    for i in range(len(listofkeys)):
        print(str(i+1) + ': ' + listofkeys[i])
    print('\nQ: Quit')
    choice = input('\nPlease enter your selection: ')

    # --------------------------- #
    # Choice selection manager
    # ----------------------------#
    if choice == '':
        print('\nOops! looks like you forgot to choose an option Chief!')
        time.sleep(2)
    elif choice == 'Q' or choice == 'q':
        sys.exit(0)
    else:
        try:
            if int(choice)-1 in range(len(listofkeys)):
                if choice == '1':
                    os.system('clear')
                    print('************ LOGIN **************' + '\n')
                    lg1.cred_harvest()
                elif choice == '2':
                    os.system('clear')
                    host_menu()
                elif choice == '3':
                    for i in selected_hosts:
                        gc1.send_command(lg1.username,lg1.password,Hosts_Dict[i],'show run')
                    input('Press ENTER to continue...')
                elif choice == '4':
                    for i in selected_hosts:
                        gc1.send_command(lg1.username,lg1.password,Hosts_Dict[i],'show vlan')
                    input('Press ENTER to continue...')
                elif choice == '5':
                    for i in selected_hosts:
                        gc1.send_command(lg1.username,lg1.password,Hosts_Dict[i],'show version')
                    input('Press ENTER to continue...')
                elif choice == '6':
                    kustom_command = input('kustom command: ')
                    for i in selected_hosts:
                        gc1.send_command(lg1.username,lg1.password,Hosts_Dict[i],kustom_command)
                    input('Press ENTER to continue...')
        except:
            print('\nInvalid option. Try agin Chief!333333333333333')
            time.sleep(2)
            menu()


def host_menu():
    # ------------------- #
    # Function Settings
    # --------------------#
    listofkeys = list(Hosts_Dict.keys())
    listofvals = list(Hosts_Dict.values())
    global selected_hosts

    # ------------------------------------ #
    # print host selection menu function
    # -------------------------------------#
    os.system('clear')
    print('************ HOST SELECT **************' + '\n')
    print(selected_hosts)
    print()
    for i in range(len(listofkeys)):
        print(str(i+1) + ': ' + listofkeys[i])
    print('\nC: Clear')
    print('Q: Quit')
    choice = input('\nSelect a host: ')

    # --------------------------- #
    # Choice selection manager
    # ----------------------------#
    if choice == '':
        print('\nOops! looks like you forgot to choose an option Chief!')
    elif choice == 'C' or choice == 'c':
        selected_hosts = []
    elif choice == 'Q' or choice == 'q':
        menu()
    else:
        try:
            if int(choice)-1 in range(len(listofkeys)):
                # print(listofkeys[int(choice)-1])
                # time.sleep(3)
                if listofkeys[int(choice)-1] not in selected_hosts:
                    selected_hosts.append(listofkeys[int(choice)-1])
                    # print(listofvals[str(listofkeys[int(choice)-1]))

                elif listofkeys[int(choice)-1] in selected_hosts:
                    selected_hosts.remove(listofkeys[int(choice)-1])
        except:
            print('\nInvalid option. Try agin Chief!')
            time.sleep(2)
        host_menu()

menu()
