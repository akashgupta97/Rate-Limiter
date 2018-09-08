
import json
import time
import ssl
import os
import urllib.parse,urllib.request,urllib.error

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

x = 1


