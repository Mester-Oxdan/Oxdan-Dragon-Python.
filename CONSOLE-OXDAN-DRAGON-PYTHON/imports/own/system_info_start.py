import imports.own.will_go_to_start
import socket
from sys import platform
from time import sleep
import os
import ctypes
from colorama import Fore
import requests

def system_info_start():

            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

            if is_admin == False:
                print("\nYou are: 'User'")
                sleep(0.01)

            elif is_admin == True:
                print("\nYou are: 'Super User/Admin'")
                sleep(0.01)

            print("Language: 'English'")
            sleep(0.01)

            if platform == "linux" or platform == "linux2":
                # linux
                print("System: 'Linux'")
                sleep(0.01)

            elif platform == "win32":
                # Windows...
                print("System: 'Windows'")
                sleep(0.01)

            else:
                print("System: 'Windows'")
                sleep(0.01)

            print("Hostname: " + socket.gethostname())
            sleep(0.01)

            hostname=socket.gethostname()   
            IPAddr=socket.gethostbyname(hostname)   
            print("IPv4 Address: "+IPAddr)
            sleep(0.01)

            def search_net(ip='127.0.0.1'):

                    response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                    print("Network Ip Address: " + Fore.WHITE + response.get('query'))
                

            response = requests.get('https://api64.ipify.org?format=json').json()
            ip = response["ip"]
                
            search_net(ip = ip)

            if platform == "linux" or platform == "linux2":
                # linux
                print("Version: 1.2023 [ENGLISH] (PYTHON) [LINUX]")
                sleep(0.01)

            elif platform == "win32":
                # Windows...
                print("Version: 1.2023 [ENGLISH] (PYTHON) [WINDOWS]")
                sleep(0.01)

            else:
                print("Version: 1.2023 [ENGLISH] (PYTHON) [WINDOWS]")
                sleep(0.01)

            imports.own.will_go_to_start.main()