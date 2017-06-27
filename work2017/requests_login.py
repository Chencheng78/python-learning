import requests
import json
from bs4 import BeautifulSoup


base_url = 'http://p.to/cgi-bin/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                         '53.0', 'Content-Type': 'application/json'}
upgrade_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/'
                         '53.0', 'Content-Type': "'multipart/form-data';boundary=--25ff681d25ed493a86bf6f97609a23fe"}
data = {"method": "set", "module": {"security": {"login": {"username": "admin", "password": "YWRtaW4%3D"}}},
        "_deviceType": "pc"}

firmware_dir = {'files': open('SW_K3C_703004744_V33.1.18.135.bin', 'rb')}
r = requests.post(base_url, data=json.dumps(data), headers=headers)
print r.headers
print r.content
# print r.read
stok = json.loads(r.content)['module']['security']['login']['stok']

upgrade_url = base_url + 'stok='+stok + '/system/upgrade'

print upgrade_url
print stok
upgrade_request = requests.post(upgrade_url,files=firmware_dir)
# reboot_r = requests.post(reboot_url, headers=headers)
