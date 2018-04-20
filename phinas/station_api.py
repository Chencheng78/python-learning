# -*- coding:utf-8 -*-

import requests
import json
import base64


class N2(object):

    def __init__(self, ipaddr):
        self.url = 'http://' + ipaddr + ':3000'

    '''
    API interaction
    
    Input: data, headers....
    Output: HTTP response content.
    '''

    def get_users(self):
        url = self.url + '/users'
        req = requests.get(url)
        return req

    def get_token(self, uuid, password):
        encode_string = 'Basic ' + base64.b64encode(uuid + ':' + password)
        b64_headers = {'Authorization': encode_string}
        url = self.url + '/token'
        req_get_token = requests.get(url, headers=b64_headers)
        return req_get_token.json()['type'] + ' ' + req_get_token.json()['token']

    def get_specific_user(self, uuid, headers):
        url = self.url + '/users/' + uuid
        req = requests.get(url, headers=headers)
        return req

    def get_drives(self, headers):
        url = self.url + '/drives'
        req = requests.get(url, headers=headers)
        return req
    '''
    Data Process
    
    Input: HTTP response.
    Output: The interested data/value.
    '''
    @staticmethod
    def user_uuid(user, user_list):
        for i in range(len(user_list)):
                if user_list[i]['username'] == user:
                    return user_list[i]['uuid']

if __name__ == '__main__':
    nas = N2('10.5.51.58')


# headers = {'User-Agent': 'node-superagent/3.8.2', 'Authorization': ''}
# auth_str = 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dWlkIjoiN2JkYWI1MDItZmY3ZC00ODJiLTkyZWEtY2JmOGE1ZWE2MWJmIn0.4c-0aTBZ_IBNQ1h8LTtHOpIAkyVM4ZIZ-U7RBi_eaHY'
#
#
# #headers['Authorization'] = auth_str
# #print headers
# r = requests.get('http://10.5.51.58:3000/users/7bdab502-ff7d-482b-92ea-cbf8a5ea61bf', headers=headers)
# print r.status_code
# print r.json()
#
# headers['Authorization'] = 'Basic ' + base64.b64encode('7bdab502-ff7d-482b-92ea-cbf8a5ea61bf:test')
# print headers
# r_get_token = requests.get('http://10.5.51.58:3000/token', headers=headers)
#
# print r_get_token.status_code
# print r_get_token.json()
# token_str = r_get_token.json()['type'] + ' ' + r_get_token.json()['token']
# print token_str
# if token_str == auth_str:
#     print 'match'
