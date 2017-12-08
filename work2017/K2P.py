from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def login_k2p(driver, url, pwd):
	driver.get(url)
	WebDriverWait(driver, 10, ignored_exceptions=True).until(lambda x: x.find_element_by_xpath(".//*[@id='Pwd']").is_displayed())
	driver.maximize_window()
	driver.find_element_by_xpath(".//*[@id='Pwd']").send_keys(pwd)
	driver.find_element_by_xpath("html/body/form/div/div[2]/button").click()
	# try:
	# 	WebDriverWait(driver, 15).until(lambda x: x.find_element_by_id("Later").is_displayed())
	# 	driver.find_element_by_id("Later").click()
	# except Exception: pass
	sleep(5)


def reboot_k2p(driver):
	WebDriverWait(driver, 10, ignored_exceptions=True).until(
		lambda x: x.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/div[2]/ul/li[2]/div/span").is_displayed())
	driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/div[2]/ul/li[2]/div/span").click()
	sleep(1)
	driver.find_element_by_xpath(".//*[@id='restart']").click()
	sleep(1)
	driver.find_element_by_xpath(".//*[@id='confirm_bt']").click()
	sleep(1)

if __name__ == '__main__':
	wdriver = webdriver.Firefox()
	wdriver.get('http://p.to')
	WebDriverWait(wdriver, 10, ignored_exceptions=True).until(lambda x: x.find_element_by_xpath(".//*[@id='admin_pwd']").is_displayed())
	wdriver.find_element_by_xpath(".//*[@id='admin_pwd']").send_keys('admin')
	wdriver.find_element_by_xpath("html/body/form/div/div[2]/button").click()
	# try:
	# 	WebDriverWait(wdriver, 15).until(lambda x: x.find_element_by_id("Later").is_displayed())
	# 	wdriver.find_element_by_id("Later").click()
	# except Exception: pass
	sleep(5)
	wdriver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/div[2]/ul/li[2]/div/span").click()
	sleep(1)
	wdriver.find_element_by_xpath(".//*[@id='restart']").click()
	sleep(1)
	wdriver.find_element_by_xpath(".//*[@id='confirm_bt']").click()
	sleep(1)
