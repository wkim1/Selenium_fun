from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import argparse
import sys

#Time to wait for the page to load
WAITING_TIME = 5
#Time to wait until trying to enroll again
REFRESH_INTERVAL = 30

username = sys.argv[1]
pw = sys.argv[2]
authcode = sys.argv[3]
className = sys.argv[4]

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://axess.sahr.stanford.edu/group/guest/simpleenroll")

usernameElem = driver.find_element_by_name("username")
usernameElem.send_keys(username)

pwElem = driver.find_element_by_name("password")
pwElem.send_keys(pw)

driver.find_element_by_name("Submit").click()

authcodeElem = driver.find_element_by_name("otp")
authcodeElem.send_keys(authcode)
authcodeElem.send_keys(Keys.RETURN)

queryElem = driver.find_element_by_name("query")
queryElem.send_keys(className)
queryElem.send_keys(Keys.RETURN)

time.sleep(WAITING_TIME)

enrollElem = driver.find_element_by_xpath("//div[contains(text(),'enroll')]")

while True:
	enrollElem.click()
	finishEnrollElem = driver.find_element_by_xpath("//div[contains(text(),'finish enrolling')]")
	finishEnrollElem.click()
	time.sleep(REFRESH_INTERVAL)

