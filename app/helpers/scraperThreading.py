import threading
import undetected_chromedriver as uc
from loguru import logger
class ScrapeThread(threading.Thread):
    def __init__(self, url, quit, headless):
        threading.Thread.__init__(self)
        logger.info("Creating new Chrome driver instance")
        logger.info(url)
        self.url = url
        self.page_source = None
        self.driver=uc.Chrome(version_main=112, headless=headless)
        logger.info("Creating new Chrome driver instance success")
        self.quit=quit
        logger.info("Quit Chrome driver instance success")
  
    def run(self):
        try:
            self.driver.get(self.url)
            self.page_source = self.driver.page_source
            if self.quit==True:
                self.driver.close()
        except:
            raise Exception("Have an exception")
    def get_page_source(self):
        return self.page_source
    def get_driver(self):
        return self.driver