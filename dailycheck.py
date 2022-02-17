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
import datetime


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
sleepy1 = random.randint(1,4)
sleepy2 = random.randint(1,4)
sleepy3 = random.randint(1,4)
sleepy4 = random.randint(1,2)

def autocheck():
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

    time.sleep(sleepy1)

    check = driver.find_element_by_xpath('/html/body/div[2]/main/div/article/div/div[1]/div[2]/div/p/a')
    check.click()

    time.sleep(sleepy2)

    continue1 = driver.find_element_by_id('continue')
    continue1.click()

    time.sleep(sleepy4)

    covidsymptoms = driver.find_element_by_id('covidsymptoms-no')
    covidsymptoms.click()

    time.sleep(sleepy4)

    contactsymptoms = driver.find_element_by_id('contactsymptoms-no')
    contactsymptoms.click()

    time.sleep(sleepy3)

    exposure = driver.find_element_by_id('exposure-no')
    exposure.click()

    time.sleep(sleepy1)

    positivetest = driver.find_element_by_id('positivetestever-no')
    positivetest.click()

    submit = driver.find_element_by_id('submit')
    submit.click()

    time.sleep(20)

autocheck()
