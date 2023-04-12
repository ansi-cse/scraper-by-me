import threading
import undetected_chromedriver as uc

class ScrapeThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.page_source = None
  
    def run(self):
        driver = uc.Chrome(version_main=112, headless=True)
        driver.get(self.url)
        self.page_source = driver.page_source
        driver.close()
    
    def get_page_source(self):
        return self.page_source