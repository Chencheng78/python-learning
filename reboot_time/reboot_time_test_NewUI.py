# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import time
import xlwt
import sys
import os
import threading
import re
import subprocess
from config import *
from Elements_Locator import *


def login(driver, url, pwd):
    driver.get(url)
    WebDriverWait(driver, 10, ignored_exceptions=True).until(lambda x: x.find_element_by_id("Pwd").is_displayed())
    driver.find_element_by_xpath(".//*[@id='Pwd']").send_keys(pwd)
    driver.find_element_by_xpath(".//*[@id='Save']").click()
    try:
        WebDriverWait(driver, 15).until(lambda x: x.find_element_by_id("Later").is_displayed())
        driver.find_element_by_id("Later").click()
    except Exception: pass
    sleep(5)


def reboot(driver):
    driver.find_element_by_id("Tool").click()
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='Con']/div[1]/ul[2]/li[1]/ul/li[1]").click()
    sleep(1)
    driver.find_element_by_xpath(".//*[@id='Pop']/div/div/input[2]").click()


def factory_reset(driver):
    driver.find_element_by_xpath(AP_FunctionSet).click()
    sleep(1)
    driver.find_element_by_xpath(BR_BackupRestore).click()
    sleep(1)
    driver.find_element_by_xpath(BR_BackupRestore_Restore).click()
    sleep(1)
    driver.find_element_by_xpath(BR_BackupRestore_Restore_Again).click()
    sleep(1)


def wireless_status():
    cmd0 = 'netsh wlan connect name=%s' % ssid
    conn_ssid = subprocess.check_output(cmd0).decode('gbk')
    sleep(1)
    a = subprocess.Popen('netsh wlan show interfaces', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    line = a.stdout.read()
    status = re.search(u'(已连接)', line.decode('gbk'))
    if status:
        return 1
    else:
        return 0


def ping_gw(t0, sheet, num):
    sleep(8)
    timeout = 200
    success_flag = 0
    while timeout > 0:
        a = subprocess.Popen('ping 192.168.2.1 -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = a.stdout.read()
        with open('ping_gw.txt', 'a') as f:
            f.write(time.ctime())
            f.write(line)
            f.close()
        loss = re.search(u'(\()(.+)( 丢失\))', line.decode('gbk'))
        # print loss.group()
        # print 'gw: %s' % loss.group(2)
        if loss.group(2) == '0%':
            success_flag += 1
            if success_flag == 3:
                t1 = time.time()
                time_gw = t1 - t0
                sheet.write(num, 0, num)
                sheet.write(num, 2, time_gw)
                break
        else:
            timeout -= 1
            if timeout == 0:
                global ret
                ret = 0
                sheet.write(num, 2, 'Timeout')
        sleep(0.1)
    print '%i:ping GW finished' % num


def ping_baidu(t0, sheet, num):
    sleep(8)
    timeout = 220
    while timeout > 0:
        a = subprocess.Popen('ping www.baidu.com -n 1', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        line = a.stdout.read()
        with open('ping_baidu.txt', 'a') as f:
            f.write(time.ctime())
            f.write(line)
            f.close()
        status = re.search(u'请求找不到主机', line.decode('gbk'))
        loss = re.search(u'(\()(.+)( 丢失\))', line.decode('gbk'))
        global ret
        if not status:
            if loss and loss.group(2) == '0%':
                t1 = time.time()
                time_baidu = t1 - t0
                sheet.write(num, 0, num)
                sheet.write(num, 3, time_baidu)
                break
            else:
                timeout -= 1
                if timeout == 0:
                    ret = 0
                    sheet.write(num, 3, 'Timeout')
                sleep(1)
            # print 'waiting for internet'
        else:
            timeout -= 1
            if timeout == 0:
                ret = 0
                sheet.write(num, 3, 'Timeout')
            sleep(1)
        # print 'waiting for DNS...%s' % timeout
    print '%i:ping internet finished' % num


def webui_finish(driver, t0, sheet, num, screenshots):
    timeout = 0
    global ret
    sleep(5)
    while timeout < 200:
        try:
            reboot_finish = driver.find_element_by_xpath(".//*[@id='Pwd']").is_displayed()
            t1 = time.time()
            time_webui = t1 - t0
            screenshots_name = screenshots + '\\success_%i.png' % num
            driver.save_screenshot(screenshots_name)
            sheet.write(num, 0, num)
            sheet.write(num, 1, time_webui)
            print '%i: WEBUI Success.' % num
            break
        except NoSuchElementException:
            timeout += 1
            # print '%s waiting for WEBUI...' % timeout
            sleep(1)
            if timeout == 300:
                ret = 0
                sheet.write(num, 1, 'Timeout')
                screenshots_name = screenshots + '\\failed_%i.png' % num
                driver.save_screenshot(screenshots_name)
                print '%i: WEBUI Failed.' % num

    print '%i: WEBUI Finished.' % num


def run_reboot(count):
    current_day = time.strftime('%Y_%m_%d', time.localtime())
    current_time = time.strftime('%H_%M_%S', time.localtime())
    root_dir = directory + '/Reboot_%s' % current_day
    #print(root_dir)
    screenshot_dir = root_dir + '/screenshot_%s' % current_time
    result_excel = root_dir + '/test_%s.csv' % current_time
    if not os.path.exists(directory):
        os.mkdir(directory)
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    os.mkdir(screenshot_dir)
    os.chdir(screenshot_dir)
    screenshot_path = os.getcwd()
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('reboot', cell_overwrite_ok=True)
    sheet.write(0, 0, 'count')
    sheet.write(0, 1, 'Reboot finish from WebUI(s)')
    sheet.write(0, 2, 'Ping through GW(s)')
    sheet.write(0, 3, 'Ping through www.baidu.com(s)')
    sheet.write(0, 4, 'Result')
    sheet.write(0, 5, 'Start time')
    book.save(result_excel)

    for i in range(1, count+1):
        driver = webdriver.Firefox()
        login(driver, 'http://p.to', 'admin')
        reboot(driver)
        t0 = time.time()
        print time.ctime(t0)
        sheet.write(i, 5, time.ctime(t0))

        if connection_type == 'wireless':
            discon = subprocess.check_output('netsh wlan disconnect').decode('gbk')
            print discon
            sleep(2)
            while wireless_status() == 0:
                print 'waiting for wireless_connection'

        threads = []
        global ret
        ret = 1
        th1 = threading.Thread(target=ping_gw, args=(t0, sheet, i))
        threads.append(th1)
        th2 = threading.Thread(target=webui_finish, args=(driver, t0, sheet, i, screenshot_path))
        threads.append(th2)
        th3 = threading.Thread(target=ping_baidu, args=(t0, sheet, i))
        threads.append(th3)
        for t in threads:
            # t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()
        # assert ret == 1
        if ret == 1:
            sheet.write(i, 4, 'Pass')
        else:
            sheet.write(i, 4, 'Fail')
        driver.close()
        book.save(result_excel)


def run_factory_reset(count):
    current_day = time.strftime('%Y_%m_%d', time.localtime())
    current_time = time.strftime('%H_%M_%S', time.localtime())
    root_dir = directory + '/Reset_%s' % current_day
    #print(root_dir)
    screenshot_dir = root_dir + '/screenshot_%s' % current_time
    result_excel = root_dir + '/test_%s.csv' % current_time
    if not os.path.exists(directory):
        os.mkdir(directory)
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    os.mkdir(screenshot_dir)
    os.chdir(screenshot_dir)
    screenshot_path = os.getcwd()
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('reset', cell_overwrite_ok=True)
    sheet.write(0, 0, 'count')
    sheet.write(0, 1, 'Reboot finish from WebUI(s)')
    sheet.write(0, 2, 'Ping through GW(s)')
    sheet.write(0, 3, 'Ping through www.baidu.com(s)')
    sheet.write(0, 4, 'Result')
    sheet.write(0, 5, 'Start time')
    book.save(result_excel)

    for i in range(1, count+1):
        driver = webdriver.Firefox()
        login(driver, 'http://p.to', 'admin')
        factory_reset(driver)
        t0 = time.time()
        print time.ctime(t0)
        sheet.write(i, 5, time.ctime(t0))

        if connection_type == 'wireless':
            discon = subprocess.check_output('netsh wlan disconnect').decode('gbk')
            print discon
            sleep(2)
            while wireless_status() == 0:
                print 'waiting for wireless_connection'

        threads = []
        global ret
        ret = 1
        th1 = threading.Thread(target=ping_gw, args=(t0, sheet, i))
        threads.append(th1)
        th2 = threading.Thread(target=webui_finish, args=(driver, t0, sheet, i, screenshot_path))
        threads.append(th2)
        # th3 = threading.Thread(target=ping_baidu, args=(t0, sheet, i))
        # threads.append(th3)
        for t in threads:
            # t.setDaemon(True)
            t.start()

        for t in threads:
            t.join()
        # assert ret == 1
        if ret == 1:
            sheet.write(i, 4, 'Pass')
        else:
            sheet.write(i, 4, 'Fail')
        driver.close()
        book.save(result_excel)


if __name__ == '__main__':
    ret = 1
    # run_factory_reset(int(sys.argv[1]))
    run_reboot(int(sys.argv[1]))
    #print wireless_status()
    # driver = webdriver.Firefox()
    # login(driver, 'http://p.to', 'admin')
    # sleep(1)
    # factory_reset(driver)
    # sleep(5)
    # driver.close()