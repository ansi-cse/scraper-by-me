import threading
import undetected_chromedriver as uc

class ScrapeThread(threading.Thread):
    def __init__(self, url, quit, headless):
        threading.Thread.__init__(self)
        self.url = url
        self.page_source = None
        self.driver=uc.Chrome(version_main=112, headless=headless)
        self.quit=quit
  
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