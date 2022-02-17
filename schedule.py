# How to use:
# 1. Install Selenium with the command: pip3 install selenium
# 2. Download the webdriver for Firefox, https://github.com/mozilla/geckodriver/releases
#       and put the geckodriver file you extract in your PATH
# 3. Either replace the netid and password variables with your actual netid and password
#       or create a bash/batch script which executes the python script with your netid
#       and password as command line arguments: python3 daily_check.py netid password
#       Replace netid and password with your netid and password

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
import time
import random

chrome_options = ChromeOptions()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
#mobile_emulation = { "deviceName": "Nexus 5" }
chrome_options.add_extension(r"C:\Program Files (x86)\buster_extension.crx")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
#chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

print("Please input the following information to automate the bot -- it will only be transmitted to Cornell University")
netid = input("Enter your netid")
password = input("Enter your password")
phone = input("Enter your phone number (continuous)")
month = input("Enter your birth month (mm)")
day = input("Enter your birth day (dd)")
year = input("Enter your birth year (yyyy)")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options = chrome_options)
driver.set_window_size(1920,1080)
driver.get("https://dailycheck.cornell.edu/")

#may need this if google flags it as a bot
#user = driver.find_element_by_xpath('//a[contains(@href,"href=/saml_login_user?redirect=%2F>")]')
userbutton = driver.find_element_by_link_text("Cornell User")
userbutton.click()

netidbutton = driver.find_element_by_id("netid")
passwordbutton = driver.find_element_by_name("password")

netidbutton.send_keys(netid)
passwordbutton.send_keys(password)

login = driver.find_element_by_name("Submit")
login.click()

scheduleit = driver.find_element_by_link_text("Schedule your test.")
scheduleit.click()

time.sleep(random.uniform(0.5,2))
first_next = driver.find_element_by_id("nextButton")
first_next.click()

registered = driver.find_element_by_name("hasPreviouslyRegistered")
registered.click()

time.sleep(random.uniform(0.4,1.8))
yesbabyyy = driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-popover/div/div[2]/ion-select-popover/ion-list/ion-radio-group/ion-item[2]')
yesbabyyy.click()

#cell = driver.find_element_by_class_name('phone-input item md item-lines-full ion-focusable item-label item-label-stacked hydrated item-interactive item-input ion-pristine ion-valid ion-touched')
#cell.send_keys(phone)

#birthday =
#birthmonth =
#birthyear =

#solving recaptcha
