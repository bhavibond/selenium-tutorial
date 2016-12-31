from selenium import webdriver
import time, unittest

class PopupControl(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
                self.base_url = "http://www.popuptest.com/"

	def test_popup(self):
		driver = self.driver
		driver.get(self.base_url)
		driver.maximize_window()
                popup = driver.find_element_by_link_text('Modeless Window')
                popup.click()
                time.sleep(5)
                driver.switch_to_window(driver.window_handles[1])
		driver.close()
                time.sleep(5)
                driver.switch_to_window(driver.window_handles[0])
		
	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()

