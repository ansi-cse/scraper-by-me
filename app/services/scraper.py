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
from pixelbin import PixelbinClient, PixelbinConfig
import asyncio
def nhaTot(url):
    try:
        t = ScrapeThread(url, True, True)
        t.start()
        t.join()
        with t.driver:
            WebDriverWait(t.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
        result=t.get_page_source()
        t.driver.close()
        return result
    except:
        t.driver.close()
        raise Exception("Have an exception")

def base(url):
    t = ScrapeThread(url, True, True)
    try:
        t.start()
        t.join()
        page_source = t.get_page_source()
        t.get_driver().close()
        return page_source
    except:
        t.get_driver().close()
        raise Exception("Have an exception")
async def bdscom(url: str):
    result=None
    try:
        loop = asyncio.get_running_loop()
        future = loop.run_in_executor(None, ScrapeThread, url, True, False)
        result = await future
        WebDriverWait(result.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__sidebar-box.re__contact-box.js__contact-box .phoneEvent.js__phone-event"))).click()
        time.sleep(15)
        pageSource=result.get_driver().page_source
        return pageSource
    except:
        traceback.print_exc()
        raise Exception("Have an exception")
    finally:
        result.get_driver().close()
# def bdscom(url):
#     t = ScrapeThread(url, False, True)
#     try:
#         t.start()
#         t.join()
#         WebDriverWait(t.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__sidebar-box.re__contact-box.js__contact-box .phoneEvent.js__phone-event"))).click()
#         time.sleep(6)
#         result=t.driver.page_source
#         t.get_driver().close()
#         return result
#     except:
#         t.get_driver().close()
#         traceback.print_exc()
#         raise Exception("Have an exception")
def bdscomInvestor(url):
    t = ScrapeThread(url, False, True)
    try:
        t.start()
        t.join()
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__btn-mobile"))).click()
        result=t.driver.page_source
        t.get_driver().close()
        return result
    except:
        t.get_driver().close()
        raise Exception("Have an exception")
def bdscomEnterpriseBroker(url):
    t = ScrapeThread(url, False, True)
    try:
        t.start()
        t.join()
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__tab-box--sm[data-value='1']"))).click()
        result=t.driver.page_source
        t.get_driver().close()
        return result
    except:
        t.get_driver().close()
        raise Exception("Have an exception")
def bdscomPersonalBroker(url):
    t = ScrapeThread("https://batdongsan.com.vn/nha-moi-gioi/", False, False)
    try:
        t.start()
        t.join()
        time.sleep(2)
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".re__tab-box--sm[data-value='0']"))).click()
        time.sleep(5)
        t.driver.get(url=url)
        time.sleep(3)
        result=t.driver.page_source
        t.get_driver().close()
        return result
    except:
        t.get_driver().close()
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
def removeWaterMask(url):
    try:
        t = ScrapeThread("https://www.watermarkremover.io/upload", False, False)
        t.start()
        t.join()
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#PasteURL__HomePage"))).click()
        inputElement= t.get_driver().find_element(By.CSS_SELECTOR,".URLInput__StyledInput-sc-10r960k-2.eZCKvY")
        inputElement.send_keys(url)
        WebDriverWait(t.get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".FilledButton__StyledButton-sc-upeeeu-0.jhrddz.URLInput__StyledButtonDesktop-sc-10r960k-3.iSbHGK"))).click()
        time.sleep(15)
        elements=t.get_driver().find_elements(By.CSS_SELECTOR,".OutputCard__ResultWrapper-sc-1ahyz78-0.fNPYcE img")
        file=getImage(elements[1].get_attribute("src"))
        t.driver.quit()
        return file
    except:
        raise Exception("Have an exception")
async def remove():
    config = PixelbinConfig({
        "domain": "https://api.pixelbin.io",
        "apiSecret": "20a231bc-cde1-4b39-881a-0a77153d9ec9",
    })
    pixelbin:PixelbinClient = PixelbinClient(config=config)
    try:
        result = asyncio.get_event_loop().run_until_complete(pixelbin.assets.listFilesAsync())
        print(result)
    except Exception as e:
        print(e)
def tests(url):
    for i in range(1, 100):
        base(url)
    return
   
    
    
    