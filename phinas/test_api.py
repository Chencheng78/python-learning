import unittest
from station_api import *


class TestN2(unittest.TestCase):

    def __init__(self):
        pass
    def test_drives_success(self):

    def test_drives_wrong_auth(self):

    def test_drives_no_auth(self):

if __name__ == '__main__':
    nas = N2('10.5.51.58')
    print nas.url
    print nas.get_user_uuid('admin')
