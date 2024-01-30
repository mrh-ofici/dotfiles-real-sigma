#!/bin/python
import re
import subprocess
from os import system
from sys import argv
def scan():
    net = subprocess.run("ifconfig", stdout=subprocess.PIPE)
    
    stdout = net.stdout.decode("utf-8")

    result1 = re.findall(r"w\w+:", stdout)
    result = str(result1).replace(':', '').replace('[', '').replace(']', '').replace('\'', '')
    if result != '':
        return result
def main():
    
    if argv[1:]:
        name = str(argv[1:]).replace('[', '').replace(']', '').replace('\'', '')
    else:
        name = 'wlan0'
    print(f'\ninterface {scan()} changed for: {name}')
    system(f"sudo ip link set {scan()} down && sudo ip link set {scan()} name {name} && sudo ip link set {name} up && sudo systemctl restart NetworkManager")
    
if __name__ == '__main__':
    main()