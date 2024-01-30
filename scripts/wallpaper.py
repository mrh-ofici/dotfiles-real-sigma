#!/bin/python
import subprocess
from time import sleep

dir = "/home/mrh/Pictures/"
count = 0
first = 0 
cache = "1"
while True:
    command = subprocess.run("bspc query -D -d focused --names", stdout=subprocess.PIPE, shell=True)
    id  = command.stdout.decode("utf-8")
    id1 = id.rstrip()+".png"
    atual = id.rstrip()
    
    if first == 0:
        subprocess.run(f"feh --bg-fill --no-fehbg {dir}{id1}", shell=True)
        first = 1
    if count > 0:
        
        count = 0
        if cache != atual:
            subprocess.run(f"feh --bg-fill --no-fehbg {dir}{id1}", shell=True)
            cache = atual
    count +=1
    
    sleep(0.1)
