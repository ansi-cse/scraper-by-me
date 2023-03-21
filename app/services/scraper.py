import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = uc.Chrome(use_subprocess=True)
def scraper(url):
    with driver:
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ShowPhoneButton_phoneButton__p5Cvt"))).click()
    return driver.page_source
   
    
    
    