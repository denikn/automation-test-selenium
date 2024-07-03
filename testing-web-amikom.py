import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebAutomation:
    def __init__(self):
        self.setup_logging()
        self.driver = None

    def setup_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def start_driver(self):
        try:
            chrome_options = Options()
            # Hilangkan headless mode untuk debugging
            # chrome_options.add_argument("--headless")  # Opsional, untuk mode headless
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.driver.maximize_window()
            self.logger.info("Browser initiated")
        except Exception as e:
            self.logger.error(f"Error starting driver: {e}")

    def apply_wait(self, seconds=10):
        try:
            if self.driver:
                self.driver.implicitly_wait(seconds)
                self.logger.info(f"Waiting for {seconds} seconds...")
            else:
                self.logger.warning("Driver is not initialized, cannot apply wait")
        except Exception as e:
            self.logger.error(f"Error in apply_wait: {e}")

    def open_main_page(self, url):
        try:
            if self.driver:
                self.driver.get(url)
                self.logger.info(f"Opened main website: {url}")
            else:
                self.logger.warning("Driver is not initialized, cannot open main page")
        except Exception as e:
            self.logger.error(f"Error opening main page: {e}")
            self.close_browser()

    # Buka menu creative park
    def click_creative_park_link(self):
        try:
            if self.driver:
                creative_park_link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='CreativePark']"))
                )
                creative_park_link.click()
                self.logger.info("Clicked 'Creative Park' menu")
            else:
                self.logger.warning("Driver is not initialized, cannot click Creative Park link")
        except Exception as e:
            self.logger.error(f"Error clicking Creative Park link: {e}")
            self.close_browser()

    # Buka menu beasiswa
    def click_beasiswa_link(self):
        try:
            if self.driver:
                beasiswa_link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='Beasiswa']"))
                )
                beasiswa_link.click()
                self.logger.info("Clicked 'Beasiswa' menu")
            else:
                self.logger.warning("Driver is not initialized, cannot click Beasiswa link")
        except Exception as e:
            self.logger.error(f"Error clicking Beasiswa link: {e}")
            self.close_browser()

    # Buka menu selengkapnya
    def click_selengkapnya_link(self):
        try:
            if self.driver:
                selengkapnya_link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='Selengkapnya…']"))
                )
                selengkapnya_link.click()
                self.logger.info("Clicked 'Selengkapnya…' menu")
            else:
                self.logger.warning("Driver is not initialized, cannot click Selengkapnya… link")
        except Exception as e:
            self.logger.error(f"Error clicking Selengkapnya… link: {e}")
            self.close_browser()

    # Buka menu selanjutnya
    def click_selanjutnya_link(self):
        try:
            if self.driver:
                selanjutnya_link = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[text()='Selanjutnya']"))
                )
                selanjutnya_link.click()
                self.logger.info("Clicked 'Selanjutnya' menu")
            else:
                self.logger.warning("Driver is not initialized, cannot click Selanjutnya link")
        except Exception as e:
            self.logger.error(f"Error clicking Selanjutnya link: {e}")
            self.close_browser()

    def close_browser(self):
        try:
            if self.driver:
                self.driver.quit()
                self.logger.info("Browser closed")
        except Exception as e:
            self.logger.error(f"Error closing browser: {e}")

if __name__ == "__main__":
    try:
        automation = WebAutomation()
        automation.start_driver()
        automation.open_main_page("https://home.amikom.ac.id")
        automation.apply_wait()
        automation.click_creative_park_link()
        automation.apply_wait()
        automation.click_beasiswa_link()
        automation.apply_wait()
        automation.click_selengkapnya_link()
        automation.apply_wait()
        # Looping 3x untuk klik "Selanjutnya"
        for _ in range(5):
            automation.click_selanjutnya_link()
            automation.apply_wait()
    finally:
        if automation:
            automation.close_browser()
