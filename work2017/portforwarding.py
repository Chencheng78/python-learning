from K3C_ui_setting import *
from time import sleep


def portforwarding_settings(method, **kwargs):
    print kwargs
    print kwargs['startport1']

if __name__ == '__main__':
    # test = K3C('admin', 'admin')
    # print test.portforwarding_enable(0)
    portforwarding_settings(1, protocol='tcp', startport=6000, endport=7000)

