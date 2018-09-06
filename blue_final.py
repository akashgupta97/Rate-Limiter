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
        "please split your csv file into two or more files,run them separately, this program is limited to the scope of at max, 14670 devs.")
    print("the first 14790 devs are being handled.")
print("usernames written")
time.sleep(t / 2)
# tester for token before we start off
token_sub_url = "https://api.github.com/rate_limit"
token_url = token_sub_url + blue_lib.token_choice()
jdata = urllib.request.urlopen(token_url, context=ctx)
jdat = jdata.read().decode()
jda = json.loads(jdat)
remaining = jda["rate"]["remaining"]
remains = remaining / 100

# all usernames in folder usernamesJson, checking for discrepancies
miss_list = []  # devs we couldnt find because invalid search cases
problem_file = open('issues.txt', 'a')
problem_file.write("Search issues \n")
discrepancy = len(os.listdir(a + '\\usernamesJson\\')) - len(usernames_urls)
if discrepancy == 0:
    pass
elif discrepancy > 0:
    time.sleep(t / 2)
    discrepancy2 = len(os.listdir(a + '\\usernamesJson\\')) - len(usernames_urls)
    if (discrepancy2 < discrepancy):
        if (discrepancy2 == 0):
            pass
        else:
            time.sleep(t)
    elif (discrepancy2 == discrepancy and discrepancy2 > 0):
        miss_list = blue_lib.search_missing_devs(FirstName, LastName, loca)
        for i in miss_list:
            problem_file.write(i)
            problem_file.write("\n")
problem_file.flush()
problem_file.close()
#################################json for all usernames is here##################
for file in os.listdir(a + '\\usernamesJson\\'):
    blue_lib.unametoJSON(file)
##################private data for all usernames is here######
##############now in batches of at max 100 usernames, we extract repos########################
problem_file = open('issurep.txt', 'a')
problem_file.write("repo issues \n")
errors = []
count = 0
rep_url_file = open('rep_list.txt', 'a')
with open('pdata.txt', 'r') as pdat:
    while (True):
        line = pdat.readline()
        count = count + 1
        if line == "":
            break
        lin = line.split('###')
        username = lin[0]
        size = lin[1]
        name = lin[2].split('_')
        fname = name[0]
        lname = name[1]
        ltion = name[2]
        blue_lib.unameToRepos(fname, lname, ltion, username, size)
        count = count + 1
        if count >= 100:
            remains = remains - 1
            if remains < 3:
                remains = blue_lib.SaturationHandler()
            count = 0
            time.sleep(15)
            file_names = os.listdir(a + '\\repos\\')
            for file in file_names:
                list_of_reps, err = blue_lib.json2repos(file)
                if len(err) != 0:
                    for j in err:
                        errors.append(j)
                for i in list_of_reps:
                    fil = file.split('_')[3]
                    fstring = 'count' + file[:-4] + '#l#' + i + '.txt'
                    po_url = '"' + 'https://api.github.com/repos/' + fil[
                                                                     :-5] + '/' + i + '/contributors' + blue_lib.token_choice() + '"'
                    command_string = 'start /B curl -s ' + po_url + ' >> ' + 'nocdata\\' + fstring
                    rep_url_file.write(command_string)
                    rep_url_file.write("\n")
            if (len(err)) == 0:
                os.remove(a + '\\repos\\' + file)
time.sleep(t)
file_names = os.listdir(a + '\\repos\\')
for file in file_names:
    list_of_reps, err = blue_lib.json2repos(file)
    if len(err) != 0:
        for j in err:
            errors.append(j)
    for i in list_of_reps:
        fil = file.split('_')[3]
        fstring = 'count' + file[:-5] + '#l#' + i + '.txt'
        po_url = '"' + 'https://api.github.com/repos/' + fil[
                                                         :-5] + '/' + i + '/contributors' + blue_lib.token_choice() + '"'
        command_string = 'start /B curl -s ' + po_url + ' >> ' + 'nocdata\\' + fstring
        rep_url_file.write(command_string)
        rep_url_file.write("\n")
    if (len(err)) == 0:
        os.remove(a + '\\repos\\' + file)
rep_url_file.flush()
rep_url_file.close()
for i in errors:
    problem_file.write(i)
    problem_file.write("\n")
problem_file.flush()
problem_file.close()

#################repos is empty and no.of.commits links are ready#################
###############number of commits########################


ct = 0
out_file = open('outp.txt', 'a')
problem_file = open('issunoc.txt', 'a')
problem_file.write("noc issues \n")
problem_file.flush()
problem_file.close()
errornoc = []
with open('rep_list.txt', 'r') as nocurls:
    while (True):
        line = nocurls.readline()
        ct = ct + 1
        if line == "":
            break
        os.system(line)
        if ct >= 100:
            remains = remains - 1
            if remains < 3:
                remains = blue_lib.SaturationHandler()
            time.sleep(t)
            ct = 0
            file_name = os.listdir(a + '\\nocdata\\')
            for file in file_name:
                fil = file.split('#l#')
                rep_name = fil[1][:-4]
                name = fil[0].split('_')
                fname = name[0]
                lname = name[1]
                ltion = name[2]
                login = name[3]
                contri = blue_lib.json2commits(file, login)
                #                if len(errn) != 0:
                #                    for j in errn:
                #                        errornoc.append(j)
                strin = fname[5:] + "," + lname + "," + ltion + "," + login + "," + rep_name + "," + str(contri)
                out_file.write(strin)
                out_file.write("\n")
                os.remove(a + '\\nocdata\\' + file)

