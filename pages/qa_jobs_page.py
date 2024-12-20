from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.common.exceptions import WebDriverException


def capture_screenshot(driver, test_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")  # Zaman damgası ekleyin
    screenshot_path = os.path.join("screenshots", f"{test_name}_{timestamp}.png")  # Screenshot yolu
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")  # Klasör yoksa oluşturun
    try:
        driver.save_screenshot(screenshot_path)  # Ekran görüntüsünü kaydedin
        print(f"Screenshot saved to {screenshot_path}")
    except WebDriverException as e:
        print(f"Failed to capture screenshot: {e}")

class QAJobsPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://useinsider.com/careers/quality-assurance/")
        self.job_list = (By.XPATH, '//*[@id="jobs-list"]')
        self.position_filter =(By.XPATH, '//*[@id="career-position-filter"]')
        self.location_filter = (By.XPATH, "//span[@aria-labelledby='select2-filter-by-location-container']")
        self.department_filter = (By.XPATH, "//button[contains(text(), 'Department')]")
        self.view_role_button = (By.LINK_TEXT, "View Role")

    def filter_jobs(self, location, department):
        # Locator for the Location dropdown
        location_dropdown = (By.ID, 'select2-filter-by-location-container')

        # Click to open the dropdown
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(location_dropdown)
        ).click()

        # Wait for dropdown options to load and click the desired option
        location_option = (By.XPATH, f'//li[contains(text(), "{location}")]')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(location_option)
        ).click()

        # Locator for the Department dropdown (similar logic for departments)
        department_dropdown = (By.ID, 'select2-filter-by-department-container')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(department_dropdown)
        ).click()

        department_option = (By.XPATH, f'//li[contains(text(), "{department}")]')
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(department_option)
        ).click()


    def check_job_list(self):
        try:
            # İş liste öğelerinin görünür olmasını bekle
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located(self.job_list)
            )
            job_elements = self.driver.find_elements(*self.job_list)
            assert len(job_elements) > 0, "No jobs found."
            print(f"[INFO] {len(job_elements)} job(s) found.")
        except Exception as e:
            print(f"[ERROR] Job list couldn't be found or is empty: {e}")

    def capture_screenshot(driver, test_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")  # Zaman damgası ekleyin
        screenshot_path = os.path.join("screenshots", f"{test_name}_{timestamp}.png")  # Screenshot yolu
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")  # Klasör yoksa oluşturun
        try:
            driver.save_screenshot(screenshot_path)  # Ekran görüntüsünü kaydedin
            print(f"Screenshot saved to {screenshot_path}")
        except WebDriverException as e:
            print(f"Failed to capture screenshot: {e}")

    def click_view_role(self):
        try:
            # Butonun görünür ve tıklanabilir olmasını bekleyin
            WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable(self.view_role_button)
            )

            # Eğer buton fare ile üzerine gelerek görünür hale geliyorsa, bu işlemi gerçekleştirin
            element = self.driver.find_element(*self.view_role_button)
            ActionChains(self.driver).move_to_element(element).click().perform()  # Hover ve tıklama

        except Exception as e:
            # Hata durumunda ekran görüntüsü alın
            self.driver.save_screenshot("screenshot.png")
            raise e