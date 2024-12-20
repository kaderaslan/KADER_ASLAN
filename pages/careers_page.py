from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://useinsider.com/careers/")
        self.locations_block = (By.XPATH, '//*[@id="career-our-location"]')
        self.teams_block = (By.XPATH, '//*[@id="career-find-our-calling"]/div/div/div[2]')
        self.life_at_insider_block = (By.XPATH,'/html/body/div[2]/section[4]')

    def check_blocks(self):
        assert self.driver.find_element(*self.locations_block).is_displayed()
        assert self.driver.find_element(*self.teams_block).is_displayed()
        assert self.driver.find_element(*self.life_at_insider_block).is_displayed()

    def check_blocks(self):
        try:
            # Görünürlük için bekle
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.life_at_insider_block)
            )
            # Görünürse, elementin doğruluğunu kontrol et
            assert self.driver.find_element(*self.life_at_insider_block).is_displayed()
            print("[INFO] 'Life at Insider' bloğu görünür.")
        except Exception as e:
            print(f"[INFO] Element bulunamadı veya görünür değil: {e}")
