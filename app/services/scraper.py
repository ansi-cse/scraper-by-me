import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from urllib.parse import urlparse
from app.helpers.scraperThreading import ScrapeThread
import traceback
import time
def nhaTot(url):
    try:
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        with t.driver:
            WebDriverWait(t.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
        result=t.get_page_source()
        t.driver.quit()
        return result
    except:
        t.driver.quit()
        raise Exception("Have an exception")

def base(url):
    t = ScrapeThread(url, True, True)
    try:
        t.start()
        t.join()
        page_source = t.get_page_source()
        t.get_driver().quit()
        return page_source
    except:
        t.get_driver().quit()
        raise Exception("Have an exception")
def bdscom(url):
    t = ScrapeThread(url, False, True)
    try:
        t.start()
        t.join()
        WebDriverWait(t.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__sidebar-box.re__contact-box.js__contact-box .phoneEvent.js__phone-event"))).click()
        time.sleep(6)
        result=t.driver.page_source
        t.get_driver().quit()
        return result
    except:
        t.get_driver().quit()
        traceback.print_exc()
        raise Exception("Have an exception")
def bdscomInvestor(url):
    t = ScrapeThread(url, False, True)
    try:
        t.start()
        t.join()
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__btn-mobile"))).click()
        result=t.driver.page_source
        t.get_driver().quit()
        return result
    except:
        t.get_driver().quit()
        raise Exception("Have an exception")
def getImage(url):
    try:
        t = ScrapeThread(url, False, True)
        t.start()
        t.join()
        parseTofileName=urlparse(url).path.split("/")
        fileName=parseTofileName[len(parseTofileName)-1]
        p = Path(fileName)
        with open(p, 'wb') as file:
            if(fileName.endswith(".svg")):
                fileToWrite=t.driver.find_element(By.TAG_NAME, 'svg').screenshot_as_png
            else:
                fileToWrite=t.driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            time.sleep(1)
            t.driver.quit()
            file.write(fileToWrite)
        return fileName
    except:
        raise Exception("Have an exception")
def tests(url):
    for i in range(1, 100):
        base(url)
    return
   
    
    
    