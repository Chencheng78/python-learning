import requests
import json
import base64
from requests_toolbelt import MultipartEncoder


headers = {'User-Agent': 'node-superagent/3.8.2',
           'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiM2I0NGM5MzEtMzRmNC00NjgwLWExYjAtMDk2M2JmZjI3MDhiIn0.t_xbbCsQPpnuLk0ZdHyGHJ0zl00TTE6bQH43BRzmSqc'}

'''
Upload New File (Same Syntax shown in Wireshark but Return Error)

    Steps 1: calculate file size and hash in local.
    Steps 2: use HTTP POST method define file name size and hash in Content-Disposition field.

'''
writedir_url = 'http://10.5.51.68:3000/drives/ebf1de04-ad79-477c-b692-388dec1f965c/dirs/ebf1de04-ad79-477c-b692-388dec1f965c/entries'
#upload_file = {'config.py': (json.dumps({'size': 28, 'sha256': '4e1bd481104cbcd1d863040722aa8c226a91c4ac8552d60fb79d31eebd529ce5'}, separators=(',', ':')),
#                             open('config.py', 'rb'), 'application/octet-stream')}
upload_file = {'config.py': (json.dumps({'size': 28, 'sha256': '4e1bd481104cbcd1d863040722aa8c226a91c4ac8552d60fb79d31eebd529ce5'}),
                             open('config.py', 'rb'), 'application/octet-stream')}
# Replace with requests extension.

# m = MultipartEncoder(
#     fields={'config.py': (json.dumps({'size': 28, 'sha256': '4e1bd481104cbcd1d863040722aa8c226a91c4ac8552d60fb79d31eebd529ce5'}), open('config.py', 'rb'), 'application/octet-stream')}
# )
# headers['content-type'] = m.content_type
# print m.to_string()

req_upload = requests.post(writedir_url, headers=headers, files=upload_file)
print(req_upload.status_code)


'''
File Download (Success)

    Steps 1: use HTTP GET method with Entries UUID and name.
    Steps 2: save the file in local.
'''
download_url = 'http://10.5.51.68:3000/drives/ebf1de04-ad79-477c-b692-388dec1f965c/dirs/ebf1de04-ad79-477c-b692-388dec1f965c/entries/7d100231-e077-40de-9b9e-7565b4b54be4?name=config.py'

req_download = requests.get(download_url, headers=headers)
with open('config1.py', 'wb') as f:
    f.write(req_download.content)

'''
Make New Directory (Success)

    Steps 1: use HTTP POST method define op code : 'mkdir' and folder name.
'''
# create a new folder named 'config'
m1 = MultipartEncoder(
    fields={'config': json.dumps({'op': 'mkdir'})}
)

headers['content-type'] = m1.content_type
#print m1.to_string()
req_mkdir = requests.post(writedir_url, headers=headers, data=m1)
print req_mkdir.status_code


'''
Rename a file/folder (Success)

    Steps 1: use HTTP POST method define op code : 'rename' and name.
    * Naming Rules: FromName|ToName;
    e.g. rename folder 'config' to 'config1' the name field should be config|config1
'''
m2 = MultipartEncoder(
    fields={'config11|config123': json.dumps({'op': 'rename'})}
)

headers['content-type'] = m2.content_type
req_mkdir = requests.post(writedir_url, headers=headers, data=m2)
print req_mkdir.status_code


'''
duplicate a file (Success)

    Steps 1: use HTTP POST method define op code : 'dup' and name.
    * Naming Rules are the same as rename.
    e.g. create a duplicate file of 'a_0_0.jpg' and name it 'a_0_023.jpg'
'''
m3 = MultipartEncoder(
    fields={'a_0_0.jpg|a_0_023.jpg': json.dumps({'op': 'dup'})}
)

headers['content-type'] = m3.content_type
req_mkdir = requests.post(writedir_url, headers=headers, data=m3)
print req_mkdir.status_code

'''
remove a file

step: use HTTP POST method define op code : 'remove' and name.


'''
m4 = MultipartEncoder(
    fields={'a_0_0.jpg': json.dumps({'op': 'remove'})}
)

headers['content-type'] = m4.content_type
req_remove = requests.post(writedir_url, headers=headers, data=m4)
print req_remove.status_code
