import requests
import json
import logging
from time import sleep
import time
import xlwt
import sys
import os
import threading
import re
import subprocess

base_url = 'http://p.to/cgi-bin/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                         '53.0', 'Content-Type': 'application/json'}
data = {"method": "set", "module": {"security": {"login": {"username": "admin", "password": "YWRtaW4%3D"}}},
        "_deviceType": "pc"}

r = requests.post(base_url, data=json.dumps(data), headers=headers)
print r.headers
print r.content
# print r.read
stok = json.loads(r.content)['module']['security']['login']['stok']

reboot_url = base_url + 'stok='+stok + '/system/reboot'

print reboot_url
print stok