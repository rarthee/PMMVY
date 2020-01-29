from selenium import webdriver
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DORMCP(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\Sahana Rangarajan\\Desktop\\Python\\Worldtimebuddy\\Pythontutorials\\Seleniumscripts\\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://training9.pmmvy-cas.nic.in/BackOffice/UserAccount/Login")
        login1=self.driver.find_element_by_id("Email").click()
        self.driver.find_element_by_id("Email").send_keys("testautomation123@mailinator.com")
        self.driver.find_element_by_id("password").click()
        self.driver.find_element_by_id("password").send_keys('P@ssw0rd')
        self.driver.find_element_by_id("btnSubmit").click()

    def test_01_DOREQMCP(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()

        self.driver.find_element_by_css_selector("input[name='NoOfChildren']").click()
        self.Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(self.Aadhaar_avaialbilty_data[3].get_attribute('value'))
        self.Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('5')

        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys('K0129189')

        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Shanthala')

    # Does Husband have aadhar card 'No'

        self.Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        print(self.Father_Aadhaar_data[3].get_attribute('value'))
        self.Father_Aadhaar_data[3].click()
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('5')

        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys('K0127191')
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Shashikanth')
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys('9989009895')
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys('HID7016')

    # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a').click()
        time.sleep(3)

    # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[6]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[1]/a').click()

    # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('801')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('15th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
    ###Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys('670647')

    # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0005099')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys('50998977667102')

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Shanthala')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

    # Submit

        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()

        self.driver.switch_to_alert().accept()

        time.sleep(3)
    # To cancel
    # driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

    # To check if the form is submitted
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        assert element.text == 'The beneficiary application form is sent for approval'

    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()