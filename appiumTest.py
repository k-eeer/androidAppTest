from appium import webdriver
import unittest,os,time


class CalculatorTestCases(unittest.TestCase):

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '10'
		desired_caps['deviceName'] = 'Pixel_XL_API_29'
		desired_caps['deviceName'] = 'Android Emulator'
		desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'info.woodsmall.calculator.apk'))
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
 
	def tearDown(self):
		"Tear down the test"
		self.driver.quit()

	def testSum(self):
		"Test the app launched and result of 9+9"
		el3 = self.driver.find_element_by_id("info.woodsmall.calculator:id/btn9")
		el3.click()
		time.sleep(3)
		el4 = self.driver.find_element_by_id("info.woodsmall.calculator:id/btnPlus")
		el4.click()
		time.sleep(3)
		el5 = self.driver.find_element_by_id("info.woodsmall.calculator:id/btn9")
		el5.click()
		time.sleep(3)
		el6 = self.driver.find_element_by_id("info.woodsmall.calculator:id/btnEqual")
		el6.click()
		time.sleep(3)
		self.driver.get_screenshot_as_file('addtionResult.png')

#---START OF SCRIPT
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCases)
	unittest.TextTestRunner(verbosity=2).run(suite)


