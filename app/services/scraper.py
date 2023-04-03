import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from pathlib import Path
from urllib.parse import urlparse

def nhaTot(url):
    driver = uc.Chrome(use_subprocess=False)
    with driver:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
    result=driver.page_source
    driver.quit()
    return result

def base(url):
    driver = uc.Chrome(use_subprocess=False)
    with driver:
        driver.get(url)
        # location=driver.execute_script("""return window.paramsMap""")
    result=driver.page_source
    driver.quit()
    return result
    
def getImage(url):
    driver = uc.Chrome(use_subprocess=False)
    with driver:
        driver.get(url)
        time.sleep(0.5)
        parseTofileName=urlparse(url).path.split("/")
        fileName=parseTofileName[len(parseTofileName)-1]
        p = Path(fileName)
        with open(p, 'wb') as file:
            t=driver.find_element(By.TAG_NAME, 'img').screenshot_as_png
            file.write(t)
    driver.quit()
    return fileName
   
    
    
    