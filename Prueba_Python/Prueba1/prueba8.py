'''
Created on 25 oct 2022

@author: zorro
'''

from sys import exit
import calendar
import time
import os
from _overlapped import NULL
from numpy.core._type_aliases import void
os.chdir(r"C:\Users\zorro\Desktop\experimentos")
import platform
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(email, password):
    """ Logging into our own profile """
   
    try:
        global driver
        options = Options()
        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        # options.add_argument("headless")
        try:
            driver = webdriver.Chrome(executable_path=r"C:\Users\zorro\AppData\Local\Programs\Python\Python310\Lib\site-packages\selenium\chromedriver.exe", options=options)
            print("you logged in. Let's rock")
        except:
            print("you need web driver!")
            exit()

        #driver.get("https://en-gb.facebook.com")
        driver.get("https://facebook.com")
        
        #driver.maximize_window()
        # filling the form

        driver.find_element(By.CSS_SELECTOR,"._9xo5 ._9xo7").click()
        driver.find_element(By.XPATH, "//input[@placeholder='Correo electrónico o número de teléfono']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys(password)
        # clicking on login button

        driver.find_element(By.NAME,"login").click()
        
    except:
        print("maybe something is wrong")
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def main():
    
    with open('credentials.txt') as f:
        email = f.readline().split('"')[1]
        password = f.readline().split('"')[1]

        if email == "" or password == "":
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit()

    ids = ["https://facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]
    if len(ids) > 0:
        print("\nStarting Scraping...")
        login(email, password)
        time.sleep(5)
        print(ids)
        driver.get(ids[0])
        print(driver.find_elements(By.CLASS_NAME,"x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u"))
        #driver.close()
    else:
        print("Input file is empty.")


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    # Let's begin
    main()