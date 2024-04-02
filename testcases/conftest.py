import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.yatra.com/")
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    time.sleep(3)
    driver.close()