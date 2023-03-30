import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import time
from pathlib import Path
driver = uc.Chrome(use_subprocess=True)
def NhaTot(url):
    with driver:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
    return driver.page_source
def Base(url):
    with driver:
        driver.get(url)
        time.sleep(5)
        # location=driver.execute_script("""return window.paramsMap""")
    return driver.page_source
def GetImage(url):
    with driver:
        driver.get(url)
        time.sleep(3)
        p = Path(url)
        with open(p, 'wb') as file:
            file.write(driver.save_screenshot(p))
    return file
   
    
    
    