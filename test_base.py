import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from config import TestConfig

class TestBase:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        if TestConfig.BROWSER.lower() == "chrome":
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # Add more browser options as needed
        
        self.driver.implicitly_wait(TestConfig.IMPLICIT_WAIT)
        self.driver.maximize_window()
        self.driver.get(TestConfig.BASE_URL)
        
        request.cls.driver = self.driver
        yield
        self.driver.quit()

    def take_screenshot(self, name):
        self.driver.save_screenshot(f"screenshots/{name}.png")