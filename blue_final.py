#Created By:- Akash
import urllib.parse,urllib.request,urllib.error
import time
import os
import ssl
import csv
import json
import blue_lib
t = 10
# if your average internet speed is below 1MBps , 
#then please increase the numerical in the speed_factor.txt by a step of 2
blue_lib.clean_slate_protocol()
try:
    file = open('speed_factor.txt', 'r')
    b = file.readline()
    file.close()
    t = int(b.rstrip().lstrip())
except:
    t = 10
file = open('pdata.txt', 'a')
file.flush()
file.close()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try:
    os.remove('outp.txt')
except:
    pass
try:
    os.remove('pdata.txt')
except:
    pass
start = time.clock()
#############start program###############################
