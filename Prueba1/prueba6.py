'''
Created on 24 oct 2022

@author: zorro
'''
from getpass import getpass
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import chrome, ChromeOptions
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/profile.php?id=100005602149811')
