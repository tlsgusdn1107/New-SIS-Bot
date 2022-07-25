from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from datetime import datetime
from pytz import timezone
import sys
import time 

usernameStr = 'REPLACE'
passwordStr = 'REPLACE'

try:
	usernameStr = sys.argv[1]
	passwordStr = sys.argv[2]
except BaseException:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py SIS_UserID SIS_Password\n\nExample: \n python bot.py cshin12 applemint\n")
	sys.exit(-1)
if '@' in usernameStr:
	print("\nError: This script should be run with the following (valid) flags:\n python bot.py SIS_UserID SIS_Password\n\nExample: \n python bot.py cshin12 applemint\n")
	sys.exit(-1) 

usernameStr += '@jh.edu'

browser = webdriver.Chrome()
browser.get(('https://sis.jhu.edu/sswf'))
nextButton = browser.find_element_by_id('linkSignIn')
nextButton.click()
WebDriverWait(browser, 10)
time.sleep(3)

username = browser.find_element_by_id('i0116')
username.send_keys(usernameStr)
nextButton2 = browser.find_element_by_id('idSIButton9')
nextButton2.click()
WebDriverWait(browser, 10)
time.sleep(3)

password = browser.find_element_by_id('i0118')
password.send_keys(passwordStr)
nextButton2 = browser.find_element_by_id('idSIButton9')
nextButton2.click()
WebDriverWait(browser, 10)
time.sleep(3)

WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "aspnetForm")))
browser.get("https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx?MyIndex=88199")
time.sleep(3)

selectAll = browser.find_element_by_id('SelectAllCheckBox')
selectAll.click()
time.sleep(3)

WebDriverWait(browser, 10)
register = browser.find_element_by_id("ctl00_contentPlaceHolder_ibEnroll")

# # Wait until its 7 O'clock (fixed to EST)
while True:
	current_hour = datetime.now(timezone('US/Eastern')).time().hour
	if current_hour == 7:
		browser.execute_script("arguments[0].click();", register)
		WebDriverWait(browser, 10000)
		while True:
			if (browser.find_element_by_id('ctl00_contentPlaceHolder_rbWaitlistYes')):
				yes = browser.find_element_by_id('ctl00_contentPlaceHolder_rbWaitlistYes')
				cont = browser.find_element_by_id('ctl00_contentPlaceHolder_cmdContinue')
				yes.click()
				WebDriverWait(browser, 10)
				cont.click()
		break
