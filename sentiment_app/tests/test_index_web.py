import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebTests(unittest.TestCase):
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(executable_path=r'C:/Users/damol/OneDrive/Life_After_UNI/Personal_Study/MARCH_APRIL/TDD/chromedriver')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:5000')

    def test_sentiment_app_name(self) ->None:
        driver = self.driver
        self.assertIn("Sentiment", driver.title)

    def tearDown(self) -> None:
        self.driver.close()