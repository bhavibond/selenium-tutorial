from selenium import webdriver
import unittest, time
import xlrd

class GoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.co.in"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_search(self):
        driver=self.driver
        driver.get(self.base_url +"/")
        driver.maximize_window()
        wbook=xlrd.open_workbook('test.xls')
        sheetname = wbook.sheet_names() 
        sheet1 = wbook.sheet_by_index(0) 
                        
        i=0
        while (i<4):
            rownum = (i)
            rows = sheet1.row_values(rownum)
            element = driver.find_element_by_id("gbqfq")
            driver.find_element_by_id("gbqfq").send_keys(rows[0])        
            element.submit()
	    time.sleep(5)
            print "The keyword [" + rows[0] + "] is searched"
            driver.back()
            time.sleep(5)
            i=i+1
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
