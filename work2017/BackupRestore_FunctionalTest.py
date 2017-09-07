from K3C_ui_setting import *
from time import sleep
import logging

ssid_24 = 'TEST0905_24'
psk_24 = '2424242424'
channel_24 = '6'
ssid_5 = 'TEST0905_5'
psk_5 = '5555555555'
channel_5 = '36'

# === Initialization === #
test = K3C('admin', 'admin')
logging.basicConfig(level=logging.INFO)

# === Step 1. Change wireless settings === #
logging.info('Config wireless 2.4G')
test.set_wireless_24g(ssid_24, psk_24, channel=channel_24)
sleep(20)
logging.info('Config wireless 5G')
test.set_wireless_5g(ssid_5, psk_5, channel=channel_5)
sleep(20)
wirelessInfo = test.get_wirelessinfo()
assert wirelessInfo['module']['wireless']['wifi_2g_config']['ssid'] == ssid_24, 'Failed to set wireless 2.4G'
assert wirelessInfo['module']['wireless']['wifi_5g_config']['ssid'] == ssid_5, 'Failed to set wireless 5G'

# === Step 2. Back-up File Download === #
logging.info('Downloading back-up file')
test.backup_download('config.dat')
sleep(5)

# === Step 3. Factory Restore === #
logging.info('Factory Restore, Wait for 200s...')
test.reset()
ProgressBar_Wait(100, 2)

# === Step 4. Router Provisioning === #
logging.info('Quick-config...')
test.register('DHCP', 'NA', 'default_24', 'default_5')
sleep(20)

# === Step 5. Back-up File Upload === #
logging.info('Back-up file uploading, Wait for 200s...')
ret = test.backup_upload('config.dat')
assert ret == 200, 'Failed to upload back-up file.'
ProgressBar_Wait(100, 2)

# === Step 6. Wireless Settings Check === #
wirelessInfo = test.get_wirelessinfo()
print wirelessInfo
logging.info('Parameter checking...')

if wirelessInfo['module']['wireless']['wifi_2g_config']['ssid'] == ssid_24 and \
   wirelessInfo['module']['wireless']['wifi_2g_config']['password'] == psk_24 and \
   wirelessInfo['module']['wireless']['wifi_2g_config']['channel'] == channel_24 and \
   wirelessInfo['module']['wireless']['wifi_5g_config']['ssid'] == ssid_5 and \
   wirelessInfo['module']['wireless']['wifi_5g_config']['password'] == psk_5 and \
   wirelessInfo['module']['wireless']['wifi_5g_config']['channel'] == channel_5:
    print 'Pass!'
else:
    print 'Fail!'
