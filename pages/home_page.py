from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://useinsider.com/")
        self.wait = WebDriverWait(driver, 20)

        # Doğru XPath kullanma
        self.COMPANY_MENU_SELECTOR = (By.XPATH, '//*[@id="navbarNavDropdown"]/ul[1]/li[6]')
        self.CAREERS_MENU_SELECTOR = (By.XPATH, "//nav//a[contains(text(), 'Careers')]")


    accept_cookies_button = (By.ID, "wt-cli-accept-all-btn")
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.accept_cookies_button)
            ).click()
        except Exception as e:
            print(f"[INFO] Çerez izni kabul edilemedi: {e}")



    def go_to_careers(self):
        # Öğenin görünür olmasını bekliyoruz ve sonra tıklıyoruz
        company_menu = self.wait.until(EC.visibility_of_element_located(self.COMPANY_MENU_SELECTOR))
        ActionChains(self.driver).move_to_element(company_menu).perform()  # Üzerine geliyoruz (hover)

        # Şimdi tıklama işlemi
        company_menu.click()

        # "Careers" menüsüne tıklıyoruz
        careers_menu = self.wait.until(EC.element_to_be_clickable(self.CAREERS_MENU_SELECTOR))
        careers_menu.click()