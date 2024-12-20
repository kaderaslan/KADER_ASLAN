import pytest
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_jobs_page import QAJobsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError("Desteklenmeyen tarayıcı! (Supported browsers: chrome, firefox)")

    driver.maximize_window()
    yield driver
    driver.quit()
def click_see_all_qa_jobs(driver):
    # "See All QA Jobs" düğmesinin locator'ı
    see_all_qa_jobs_button = (By.XPATH, '//a[contains(text(), "See all QA jobs")]')

    # Düğmeyi bulup tıklama işlemi
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(see_all_qa_jobs_button)
    ).click()


def test_insider_career_page(driver):
    # Step 1: Open Insider home page
    home_page = HomePage(driver)
    home_page.accept_cookies()

    # Step 2: Navigate to Careers page
    home_page.go_to_careers()
    careers_page = CareersPage(driver)
    careers_page.check_blocks()  # Check if Locations, Teams, and Life at Insider blocks are visible

    # Step 3: Navigate to QA Jobs page
    qa_jobs_page = QAJobsPage(driver)
    driver.get("https://useinsider.com/careers/quality-assurance/")
    click_see_all_qa_jobs(driver)
    home_page.accept_cookies()
    time.sleep(10)
    # Step 4: Filter jobs by Location and Department
    qa_jobs_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")
    qa_jobs_page.check_job_list()  # Check the job list
    time.sleep(10)
    # Step 5: Click "View Role" button and verify redirect
    qa_jobs_page.click_view_role()

