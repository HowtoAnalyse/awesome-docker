# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 16:27:05 2018

@author: sara.zeng
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://howtoanalyse.github.io/Reddit-Weekly-Digests/")
sleep(15)
driver.get_screenshot_as_file('selenium_testing.png') 

driver.quit()