import requests
import json
import base64
from requests_toolbelt import MultipartEncoder

headers = {'User-Agent': 'node-superagent/3.8.2',
           'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiM2I0NGM5MzEtMzRmNC00NjgwLWExYjAtMDk2M2JmZjI3MDhiIn0.t_xbbCsQPpnuLk0ZdHyGHJ0zl00TTE6bQH43BRzmSqc',
           'content-type': ''}

writedir_url = 'http://10.5.51.68:3000/drives/ebf1de04-ad79-477c-b692-388dec1f965c/dirs/ebf1de04-ad79-477c-b692-388dec1f965c/entries'
