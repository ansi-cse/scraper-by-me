import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pathlib import Path
from urllib.parse import urlparse
from app.helpers.chromeDriverPool import ScrapeThread

def nhaTot(url):
    driver = uc.Chrome(use_subprocess=False,headless=True)
    with driver:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
    result=driver.page_source
    driver.quit()
    return result
def base(url):
    try:
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        page_source = t.get_page_source()
        return page_source
    except:
        raise Exception("Have an exception")

def bdscom(url):
    try:
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        WebDriverWait(t.driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__sidebar-box.re__contact-box.js__contact-box .phoneEvent.js__phone-event"))).click()
        result=t.driver.page_source
        return result
    except:
        raise Exception("Have an exception")

def bdscomInvestor(url):
    try:
        t = ScrapeThread(url, False, True)
        t.start()
        t.join()
        WebDriverWait(t.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__btn-mobile"))).click()
        result=t.driver.page_source
        t.driver.quit()
        return result
    except:
        t.driver.close()
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
            t.driver.close()
            file.write(fileToWrite)
        return fileName
    except:
        raise Exception("Have an exception")

    # driver = uc.Chrome(use_subprocess=False,headless=True)
    # with driver:
    #     driver.get(url)
    #     time.sleep(1)
    #     parseTofileName=urlparse(url).path.split("/")
    #     fileName=parseTofileName[len(parseTofileName)-1]
    #     p = Path(fileName)
    #     with open(p, 'wb') as file:
    #         t=driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
    #         file.write(t)
    # driver.quit()
    # return fileName

def tests(url):
    for i in range(1, 100):
        base(url)
    return
   
    
    
    