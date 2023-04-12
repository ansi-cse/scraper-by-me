import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pathlib import Path
from urllib.parse import urlparse
from loguru import logger
from multiprocessing.pool import ThreadPool as Pool
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
    t = ScrapeThread(url)
    t.start()
    t.join()
    page_source = t.get_page_source()
    return page_source

def bdscom(url):
    driver = uc.Chrome(use_subprocess=False, headless=True)
    with driver:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".phoneEvent.js__phone-event"))).click()
    result=driver.page_source
    driver.quit()
    return result
    
def getImage(url):
    driver = uc.Chrome(use_subprocess=False,headless=True)
    with driver:
        driver.get(url)
        time.sleep(1)
        parseTofileName=urlparse(url).path.split("/")
        fileName=parseTofileName[len(parseTofileName)-1]
        p = Path(fileName)
        with open(p, 'wb') as file:
            t=driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            file.write(t)
    driver.quit()
    return fileName

def tests(url):
    for i in range(1, 100):
        base(url)
    return
   
    
    
    