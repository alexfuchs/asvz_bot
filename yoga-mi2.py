#!/home/<user>/asvz_bot_python/bin/python

############################# Edit this: ######################################

# ETH credentials:
username = "22999"
password = "Alex1234"
# sportfahrplan_particular = 'https://www.asvz.ch/426-sportfahrplan?f[0]=sport:45750&f[1]=instructor:2588'
# all class silvia
# sportfahrplan_particular = 'https://www.asvz.ch/426-sportfahrplan?f[0]=instructor:2588'
# Yoga Montag 29 Juni 07:15 89516 89517 89518 ... CAB Move
# Body Balance Dienstag 23 Juni 12:05 96496 96497 96498 ...
# Yoga Mittwoch 24 Juni 08:15 94222 94223 94224 ... CAB Move
# Yoga Mittwoch 24 Juni 18:10 96760 96761 96762 ... Hönggerberg
# Yoga Samstag  27 Juni 10:20  97572 97573 97574 ... Foyer

###############################################################################

import time
import sys
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument(dest="argument1", help="This is the first argument")


# Parse and print the results
args = parser.parse_args()
print(args.argument1)
sportfahrplan_particular = "https://schalter.asvz.ch/tn/lessons/%s" % args.argument1
# sportfahrplan_particular = '%s' % args.argument1
# view raw

log = open("myprog.log", "a")
sys.stdout = log


def asvz_enroll():
    options = Options()
    # uncomment to see firefox popping up and work ;-)
    options.add_argument("-headless")
    # options.log.level = "trace"
    options.log.level = "error"
    # options.add_argument("--private") #open in private mode to avoid different login scenario
    driver = webdriver.Firefox(
        options=options, executable_path=r"/usr/local/bin/geckodriver"
    )

    try:

        driver.get(sportfahrplan_particular)
        driver.implicitly_wait(5)  # wait 20 seconds if not defined differently
        print("Firefox Initialized")
        time.sleep(5)
        WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Login']"))
        ).click()
        # find username and password button, send
        driver.implicitly_wait(7)  # wait 20 seconds if not defined differently
        # driver.find_element_by_xpath("//input[@id='AsvzId']").send_keys(username)
        driver.find_element_by_xpath("//input[@placeholder='ASVZ-ID']").send_keys(
            username
        )
        # driver.find_element_by_xpath("//input[@id='Password']").send_keys(password)
        driver.find_element_by_xpath("//input[@placeholder='Passwort']").send_keys(
            password
        )
        driver.implicitly_wait(7)  # wait 20 seconds if not defined differently
        # now press login button
        driver.find_element_by_xpath(
            "//button[@class='btn btn-primary btn-block']"
        ).click()

        driver.implicitly_wait(8)  # wait 20 seconds if not defined differently
        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@id='btnRegister' and @class='btn-primary btn enrollmentPlacePadding']",
                )
            )
        ).click()

        driver.implicitly_wait(10)  # wait 20 seconds if not defined differently
        print("Successfully enrolled. Train hard and have fun!")
    except:  # using non-specific exceptions, since there are different exceptions possible: timeout, element not found because not loaded, etc.
        driver.quit()
        raise  # re-raise previous exception

    driver.quit  # close all tabs and window
    return True


# run enrollment script:
i = 0  # count
success = False
success = asvz_enroll()
