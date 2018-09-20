
import json
import time
import ssl
import os
import urllib.parse,urllib.request,urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = 1


def SaturationHandler():
    global x
    token1 = "?access_token=3414d03eae8c6269c5ed05de563d22019087eda3"
    token2 = "?access_token=1aa60130f9d7d215846b32b0dcdbca82372488c4"
    token3 = "?access_token=478830ab3761e8824f7f454bec92b19958308038"
    token_sub_url = "https://api.github.com/rate_limit"
    token1_url = token_sub_url + token1
    token2_url = token_sub_url + token2
    token3_url = token_sub_url + token3
    t1 = urllib.request.urlopen(token1_url, context=ctx)
    t2 = urllib.request.urlopen(token2_url, context=ctx)
    t3 = urllib.request.urlopen(token3_url, context=ctx)
    tdata1 = t1.read().decode()
    tdata2 = t2.read().decode()
    tdata3 = t3.read().decode()
    tjs1 = json.loads(tdata1)
    tjs2 = json.loads(tdata2)
    tjs3 = json.loads(tdata3)
    remaining1 = tjs1["rate"]["remaining"]
    remaining2 = tjs2["rate"]["remaining"]
    remaining3 = tjs3["rate"]["remaining"]
    time1 = tjs1["rate"]["reset"]
    time2 = tjs2["rate"]["reset"]
    time3 = tjs3["rate"]["reset"]
    if (remaining1 <= 110 and remaining2 <= 110 and remaining3 <= 110):
        tn = time.time()
        sleep_time = min(time1 - tn, time2 - tn, time3 - tn)
        print(
            "Our tokens have reached a temporary saturation of allowed requests, sleeping till more requests are allowed")
        print("we have to stop requesting for ", sleep_time, " seconds to resume")
        time.sleep(sleep_time)
    elif (x == 1):
        if (remaining2 >= remaining3):
            x = 2
            return remaining2 / 100
        else:
            x = 3
            return remaining3 / 100
    elif (x == 2):
        if (remaining1 >= remaining3):
            x = 1
            return remaining1 / 100
        else:
            x = 3
            return remaining3 / 100
    else:
        if (remaining1 >= remaining2):
            x = 1
            return remaining1 / 100
        else:
            x = 2
            return remaining2 / 100
    print("token has been changed to", x)


def token_choice():
    token1 = "?access_token=3414d03eae8c6269c5ed05de563d22019087eda3"
    token2 = "?access_token=1aa60130f9d7d215846b32b0dcdbca82372488c4"
    token3 = "?access_token=478830ab3761e8824f7f454bec92b19958308038"
    if (x == 1):
        token = token1
    elif (x == 2):
        token = token2
    else:
        token = token3

    return token


