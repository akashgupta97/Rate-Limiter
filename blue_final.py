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
a = str(os.getcwd())
try:
    os.mkdir(a + "\\usernamesJson")
except:
    pass
try:
    os.mkdir(a + "\\repos")
except:
    pass
try:
    os.mkdir(a + "\\nocdata\\")
except:
    pass
inp = 'input.csv'
api_saturation_message_length = 137
fields = []
rows = []
csvfile = open(inp, 'r')
csvreader = csv.reader(csvfile)
fields = next(csvreader)
FirstName = []
LastName = []
Location = []
loca = []
url_missed_out_noc = []
url_missed_out_rdata = []
while (True):
    try:
        row = next(csvreader)
        if row[0] != None:
            FirstName.append(row[0])
        else:
            FirstName.append(None)
        if row[1] != None:
            LastName.append(row[1])
        else:
            LastName.append(None)
        if row[2] != None:
            Location.append(row[2])
            if row[2] == "":
                loca.append("World")
            else:
                loca.append(row[2].replace(' ', '').replace(',', '-'))
        else:
            Location.append(None)
    except:
        break
csvfile.close()
mystring = []
mystring = blue_lib.getName_location(FirstName, LastName, Location)
usernames_urls = blue_lib.username_query_generator(mystring)
# has all the urls, hit legacy
print("program might sleep to prevent readwrite buffer bottlenecks")
if len(usernames_urls) < 4990:
    blue_lib.legacy_search(usernames_urls, FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
elif len(usernames_urls) < 9980 and len(usernames_urls) >= 4990:
    blue_lib.legacy_search(usernames_urls[0:4990], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    blue_lib.legacy_search(usernames_urls[4991:9980], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
elif len(usernames_urls) < 14970 and len(usernames_urls) >= 9980:
    blue_lib.legacy_search(usernames_urls[0:4990], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    blue_lib.legacy_search(usernames_urls[4991:9980], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    blue_lib.legacy_search(usernames_urls[9981:14670], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
else:
    blue_lib.legacy_search(usernames_urls[0:4990], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    blue_lib.legacy_search(usernames_urls[4991:9980], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    blue_lib.legacy_search(usernames_urls[9981:14670], FirstName, LastName, loca)
    time.sleep(t)
    blue_lib.SaturationHandler()
    print(
