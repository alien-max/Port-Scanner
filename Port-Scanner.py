import socket
import os
import sys
import time
from colorama import Fore,init
init()

#
# Banner
#
os.system("cls")
print(Fore.RED+"""

░░░▓▓▓▓▓▓▓     ░░▓    ░░▓▓▓▓▓▓▓▓▓▓ ░░▓▓▓▓▓▓▓▓▓▓▓▓       ░▓▓▓       ▓▓▓▓         ▓▓░          ▓▓▓░░  ▓▓▓░░     ▓▓▓░░  ▓▓▓░░  ▓▓▓▓▓▓▓░▓▓▓▓▓▓▓▓▓▓▓░░░
  ░░░▓▓ ░░▓▓░░░▓▓░░▓▓       ░▓▓ ░░▓▓░      ░░▓▓       ░▓▓   ▓    ▓▓    ▓       ▓▓░▓░        ▓▓░▓▓░░ ▓▓░▓░░   ▓▓░▓▓░░ ▓▓░▓░░▓▓░░   ▓░░     ▓▓░░ ▓▓░░░
 ░░░▓▓ ░░▓▓░░▓▓    ░░▓▓   ░░▓▓ ░░▓▓ ░     ░░▓▓         ░▓▓     ▓▓             ▓▓░ ▓▓░       ▓▓░░▓▓░░▓▓░░     ▓▓░░▓▓░░▓▓░░   ▓▓▓▓░░       ▓▓░░ ▓▓░░░
 ░░░▓▓▓▓▓  ░░▓▓    ░░▓▓  ░░▓▓▓▓▓▓   ░    ░░▓▓       ░▓   ▓▓    ▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓░    ▓▓░░  ▓▓░▓▓░░    ▓▓░░  ▓▓░▓▓░░  ▓▓░░         ▓▓▓▓▓▓░░░
 ░░░▓▓      ░░▓▓ ░░▓▓    ░░▓▓ ▓▓    ░  ░░░▓▓         ░▓    ▓▓  ░ ▓▓    ▓  ▓▓░ ▓░ ░ ▓▓░  ▓▓░▓▓░░   ▓▓▓░░  ▓▓░▓▓░░   ▓▓▓░░  ▓▓▓░░ ▓░░     ▓▓░▓▓░░░
 ░░░▓░      ░ ░░▓▓▓▓    ░▓▓▓    ▓▓  ░ ░░▓▓▓▓         ░░▓▓▓▓▓   ░  ░▓▓▓▓   ░ ▓▓░  ░ ░░▓░   ▓▓░ ░    ░ ░     ▓▓░░░    ░░     ▓▓▓▓▓▓░░   ▓▓▓░░  ▓▓░░░
 ░░ ░      ░ ░░ ░░     ░ ░░    ░░  ░ ░ ░░░░          ░  ░░░    ░  ░░░░░   ░ ░░   ░  ░░    ░░  ░    ░░      ░░  ░     ░░░    ░░  ░░     ░░░    ░░ ░
  ░  ░    ░  ░  ░      ░  ░   ░    ░░  ░             ░░  ░        ░░  ░   ░  ░   ░  ░      ░░    ░░        ░   ░      ░     ░   ░ ░    ░  ░    ░ ░
  ░   ░   ░  ░            ░    ░    ░   ░             ░  ░░       ░   ░   ░  ░      ░       ░    ░         ░   ░     ░      ░  ░  ░    ░  ░    ░░
  ░       ░                    ░       ░              ░   ░           ░   ░          ░      ░              ░  ░       ░    ░  ░   ░   ░░  ░   ░░
≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠
**                                                                                                                                                  **
**                                                              Alien Max                                                                           **
**                                                                                                                                                  **
≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠≠
https://alien-max.github.io/
 """)

# 
# Menu
#
time.sleep(0.1)
print(Fore.RED + "---[ " + Fore.LIGHTYELLOW_EX + "Wellcome To Port Scanner\n")

time.sleep(0.1)
print(Fore.RED + "---[ " + Fore.LIGHTYELLOW_EX + "Choose one of the following options\n")

time.sleep(0.1)
print(Fore.YELLOW + "[1] TCP Ports Scan")

time.sleep(0.1)
print(Fore.YELLOW + "[2] UDP Ports Scan")

time.sleep(0.1)
print(Fore.YELLOW + "[3] EXIT\n" + Fore.WHITE + "\n")

number = input("---: ")

# 
# Importing Ports
# 
TCP_PORTS = []
UDP_PORTS = []

tcp_ports_file = open('tcp-ports.txt', 'r')
udp_ports_file = open('udp-ports.txt', 'r')

tcp_ports_file_content = tcp_ports_file.read()
udp_ports_file_content = udp_ports_file.read()

for i in tcp_ports_file_content:
    TCP_PORTS.append(i)

for i in udp_ports_file_content:
    UDP_PORTS.append(i)

# 
# Process
# 
# # TCP Scan
if number == "1" :
    print(Fore.RED + "\n---[ " + Fore.LIGHTYELLOW_EX + "Enter IP(v4) or Domain" + Fore.WHITE + "")
    remoteserver = input("---: ")
    remoteserverip = socket.gethostbyname(remoteserver)
    time.sleep(1)
    print(Fore.RED + "\n---[ " + Fore.LIGHTYELLOW_EX + "Entered IP(v4)\n" + Fore.WHITE + "---: " + str(remoteserverip))

    for port in TCP_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteserverip, port))
        if result == 0 :
            print(Fore.GREEN + "[+] port " + Fore.BLUE + str(port) + Fore.GREEN + " is open")
        else:
            print(Fore.RED + "[-] port " + Fore.BLUE + str(port) + Fore.RED + " is closed")

# 
# # UDP Scan
elif number == "2" :
    print(Fore.RED + "\n---[ " + Fore.LIGHTYELLOW_EX + "Enter IP(v4) or Domain" + Fore.WHITE + "")
    remoteserver = input("---: ")
    remoteserverip = socket.gethostbyname(remoteserver)
    time.sleep(1)
    print(Fore.RED + "\n---[ " + Fore.LIGHTYELLOW_EX + "Entered IP(v4)\n" + Fore.WHITE + "---: " + str(remoteserverip))

    for port in UDP_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = sock.connect_ex((remoteserverip, port))
        if result == 0 :
            print(Fore.GREEN + "[+] port " + Fore.BLUE + str(port) + Fore.GREEN + " is open")
        else:
            print(Fore.RED + "[-] port " + Fore.BLUE + str(port) + Fore.RED + " is closed")

# 
# # Exit
elif number == "3" :
    sys.exit()

else :
    print(Fore.RED + "Wrong !!!")
    time.sleep(1)
    sys.exit()

