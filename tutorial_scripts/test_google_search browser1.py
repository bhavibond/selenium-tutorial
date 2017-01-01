from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time, unittest

class BrowserTest1(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_Google_Search_FF(self):
		driver = self.driver
		driver.get("http://www.google.co.in")
		Element = driver.find_element_by_name("q")
		Element.send_keys("Alia Bhatt")
		Element.submit()
		time.sleep(20)
		self.assertEqual("Alia Bhatt - Google Search",driver.title)
		
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
