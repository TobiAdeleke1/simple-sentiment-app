import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class WebTests(unittest.TestCase):
    def setUp(self) -> None:
        # self.driver = webdriver.Chrome(executable_path=r'C:/Users/damol/OneDrive/Life_After_UNI/Personal_Study/MARCH_APRIL/TDD/chromedriver')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:5000')

    def test_sentiment_app_name(self) ->None:
        selenium_chrome = self.driver
        self.assertIn("Sentiment", selenium_chrome.title)
    
    def test_page_heading_is_named_sentiment_analysis(self):
        heading = self._find('heading').text
        self.assertEqual("Sentiment Analysis", heading)

    def test_page_has_input_text(self):
        input_text = self._find('large-text').text
        self.assertIsNotNone(input_text)

    def test_page_has_submit_button(self):
        submit_button = self._find('submit-button')
        self.assertIsNotNone(submit_button)
    
    def _find(self,val):
        data_attribute = f'[test-id="{val}"]'
        element = self.driver.find_element(By.CSS_SELECTOR, data_attribute)  
        return element


    def tearDown(self) -> None:
        self.driver.close()