from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException, \
WebDriverException
import unittest, time


class GmailTest(unittest.TestCase):
	def setUp(self):
	    self.driver = webdriver.Firefox()
	    self.driver.implicitly_wait(10)
	    self.base_url = "http://www.gmail.com/"
	    self.email_id = email_id # This can be a test account email id
	    self.passw = passw # This can be a test account password
            self.to_email = email # This can be a to email address
            self.subject = subject # This can be a subject
                
	def test_gmail(self):
	    driver=self.driver
	    driver.get(self.base_url)
	    driver.maximize_window()
	    sign_in_link = driver.find_elements_by_link_text('Sign in')
	    if sign_in_link:
	        sign_in_link[0].click()
	    self.driver.find_element_by_id('Email').send_keys(self.email_id)
	    self.driver.find_element_by_id('Passwd').send_keys(self.passw)
	    stay_signed_in = driver.find_element_by_id('PersistentCookie')
	    if stay_signed_in.is_selected():
	        stay_signed_in.click()
	    self.driver.find_element_by_id('signIn').click()
	    time.sleep(10)
            self.driver.find_element_by_xpath(
                "//div[@role='button' and text()='COMPOSE']").click()
            self.driver.find_element_by_name('to').send_keys(self.to_email)
            self.driver.find_element_by_name('subjectbox').send_keys(self.subject)
            self.driver.find_element_by_xpath("//div[text()='Send']").click()
            wait = WebDriverWait(self.driver, 60)
            xpath = "//div[starts with(text(), " "'Your message has been sent.')]"
            wait.until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath))
	    self.driver.get('https://mail.google.com/mail/?logout')
	    try:
	        self.driver.switch_to_alert().accept()
	    except (NoAlertPresentException, WebDriverException):
		pass
	    finally:
		self.driver.switch_to_default_content()
    
	def tearDown(self):
	    self.driver.quit()

if __name__ == "__main__":
	unittest.main()
