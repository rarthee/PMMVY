from selenium import webdriver
import unittest
import time
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from random import randint


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
        #Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()

        #No of children
        self.no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        self.no_of_children[0].click()

        self.Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(self.Aadhaar_avaialbilty_data[3].get_attribute('value'))
        self.Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('5')

        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        altnum = value = randint(1, 9999999)
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(altnum)

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
        altid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(altid)
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Shashikanth')
        phone=''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        healthid=''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

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
    #Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

    # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0005099')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Shanthala')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

    # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)

        self.driver.switch_to.alert.accept()

        time.sleep(5)
    # To cancel
    # driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

     #To check if the form is submitted
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'

        time.sleep(5)
        time.sleep(5)
    def test_02_DORGTMCP(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()

        # No. of childrens
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(Aadhaar_avaialbilty_data[3].get_attribute('value'))
        Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('3')

        # Ration card
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        altnum = value = randint(1, 9999999)
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(altnum)

        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Jyothi Kundar')

        # Does Husband have aadhar card 'No'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        print(Father_Aadhaar_data[3].get_attribute('value'))
        Father_Aadhaar_data[3].click()
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('3')
        # Voter id
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        altnum = value = randint(1, 9999999)
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(altnum)
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Jitendra Kundar')
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('1')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2] ').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()

        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('790')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('9th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Irulam ')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        ###Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys('670646')

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Jyothi Kundar')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(3)
        # To cancel
        # driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

        # To check if the form is submitted
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        time.sleep(5)
        time.sleep(5)
    def test_03_DORGTMCP(self):
       
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[7]/a').click()

        # No. of childrens
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(Aadhaar_avaialbilty_data[3].get_attribute('value'))
        Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('3')

        # Ration card
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        altnum=value = randint(1, 9999999)
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys('8975690')

        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Harini M')

        # Does Husband have aadhar card 'No'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        print(Father_Aadhaar_data[3].get_attribute('value'))
        Father_Aadhaar_data[3].click()
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('3')
        # Voter id
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        altnum = value = randint(1, 9999999)
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(altnum)
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Harsha M')
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('2')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2] ').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()

        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('791')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('10th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Irulam ')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        ###Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys('670645')

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys('701926837947981')

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Harini M')
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(3)
        # To cancel
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

        # To check if the form is submitted
        element = self.driver.find_element_by_xpath('//*[@id="spnPregnancyDate"]/span')
        time.sleep(5)
        assert element.text == 'Date of Reg of MCP card must not exceed the Beneficiary Registration Date. Please enter the correct date'
        time.sleep(5)

    def test_04_MCPGTLMP(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()

        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(Aadhaar_avaialbilty_data[3].get_attribute('value'))
        Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('2')

        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        altid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(altid)

        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Garima Thakur')

        # Does Husband have aadhar card 'No'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        Father_Aadhaar_data[3].click()
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('2')

        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        altid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(altid)
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Girish Thakur')
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[2]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('788')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('5th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        # Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Garima Thakur')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        # To cancel
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

        # To check if the form is submitted
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'

        time.sleep(5)
        time.sleep(5)
    def test_05_MCPGTLMP(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[4]/a').click()

        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        print(Aadhaar_avaialbilty_data[3].get_attribute('value'))
        Aadhaar_avaialbilty_data[3].click()
        select = Select(self.driver.find_element_by_id('beneficiaryAltID'))
        select.select_by_value('2')

        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').click()
        altid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        self.driver.find_element_by_xpath('//*[@id="txtAlternateNumber"]').send_keys(altid)

        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').click()
        self.driver.find_element_by_xpath('//*[@id="NameAsInIDCard"]').send_keys('Nandini Bhat')

        # Does Husband have aadhar card 'No'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        Father_Aadhaar_data[3].click()
        select = Select(self.driver.find_element_by_id('fatherAltID'))
        select.select_by_value('2')

        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').click()
        altid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        self.driver.find_element_by_xpath('//*[@id="txtFatherAlternateNumber"]').send_keys(altid)
        self.driver.find_element_by_xpath('//*[@id="FNameAsInIDCard"]').send_keys('Nakul Bhat')
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[2]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[6]/a').click()

        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('789')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('6th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        # Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Garima Thakur')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        # To cancel
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[2]').click()

        # To check if the form is submitted
        element = self.driver.find_element_by_xpath('//*[@id="spnPregnancyDate"]/span')
        time.sleep(5)
        assert element.text == 'Date of Reg of MCP card must not be before LMP Date. Please enter the correct date'
        time.sleep(5)

        time.sleep(5)
#LMP not provided-Eligible for all installments
    def test_06_LMPNTPRALLINS(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        # Does benficiary have Aadhaar -'Yes'
        print(Aadhaar_avaialbilty_data[2].get_attribute('value'))
        Aadhaar_avaialbilty_data[2].click()

        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').send_keys('Shamali')

        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').click()
        # aadno = ''.join(random.choice('99123456789') for i in range(12))
        # self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno)
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys('919417555234')

        # Does Husband have aadhar card 'yes'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        Father_Aadhaar_data[2].click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').send_keys('Sagar')
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').click()
        # aadno = ''.join(random.choice('99123456789') for i in range(12))
        # self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(aadno)
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys('931215223745')

        # Is the P.O/ Bank Account Aadhaar Seeded?
        PO_bank_acc = self.driver.find_elements_by_xpath('//*[@id="IsBankAccountAadhaarSeededValue"]')
        time.sleep(3)
        PO_bank_acc[0].click()

        # Phone number
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP
        self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a').click()
        time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[6]/a').click()

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
        # Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Shamali')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        time.sleep(5)
        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        time.sleep(5)
# LMP not provided-Eligible for only 3rd installment
    def test_07_LMPNTPR3RDINS(self):
        self.driver.find_element_by_xpath('//*[@id="btnNewbeneficiary"]').click()
        time.sleep(3)
        # Registration date
        self.driver.find_element_by_xpath('//*[@id="dpicker1"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[3]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

        # No of children
        no_of_children = self.driver.find_elements_by_xpath('//*[@id="NoOfChildren"]')
        no_of_children[0].click()

        Aadhaar_avaialbilty_data = self.driver.find_elements_by_xpath("//input[@id='BeneficiaryAadharExistVal']")
        time.sleep(3)
        # Does benficiary have Aadhaar -'Yes'
        print(Aadhaar_avaialbilty_data[2].get_attribute('value'))
        Aadhaar_avaialbilty_data[2].click()

        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtNameAsInAadhar"]').send_keys('Sumona')

        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').click()
        # aadno = ''.join(random.choice('99123456789') for i in range(12))
        # self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys(aadno)
        self.driver.find_element_by_xpath('//*[@id="txtAadhar"]').send_keys('230549435787')

        # Does Husband have aadhar card 'yes'

        Father_Aadhaar_data = self.driver.find_elements_by_xpath("//input[@id='FatherAadharExistVal']")
        time.sleep(3)
        Father_Aadhaar_data[2].click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtFNameAsInAadhaar"]').send_keys('Saketh')
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').click()
        # aadno = ''.join(random.choice('99123456789') for i in range(12))
        # self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys(aadno)
        self.driver.find_element_by_xpath('//*[@id="txtFAadhar"]').send_keys('931215223746')

        # Is the P.O/ Bank Account Aadhaar Seeded?
        PO_bank_acc = self.driver.find_elements_by_xpath('//*[@id="IsBankAccountAadhaarSeededValue"]')
        time.sleep(3)
        PO_bank_acc[0].click()

        # Phone number
        phone = ''.join(random.choice('0123456789') for i in range(10))
        self.driver.find_element_by_xpath('//*[@id="Phone"]').send_keys(phone)
        select1 = Select(self.driver.find_element_by_xpath('//*[@id="Category"]'))
        select1.select_by_index('3')
        healthid = ''.join(random.choice('0123ABC') for i in range(7))
        self.driver.find_element_by_xpath('//*[@id="HealthId"]').send_keys(healthid)

        # Date of LMP not entered for this test case
        # self.driver.find_element_by_xpath('//*[@id="dpicker2"]').click()
        # self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        # self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()
        # self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[2]/a').click()
        # time.sleep(3)

        # Date of registration of MCP

        self.driver.find_element_by_xpath('//*[@id="dpicker3"]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[2]/option[7]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/div/div/select[1]/option[2]').click()
        self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[3]/td[5]/a').click()

        # Present Address

        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys('802')

        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine2"]').send_keys('16th Cross')

        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').click()
        self.driver.find_element_by_xpath('//*[@id="AddressLine3"]').send_keys('Bull Temple Road')

        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').click()
        self.driver.find_element_by_xpath('//*[@id="AreaLocalitySector"]').send_keys('Alankady')

        select = Select(self.driver.find_element_by_xpath('//*[@id="drpAnganvaadi"]'))
        # Temp data
        select.select_by_index('6')
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').click()
        pin = ''.join(random.choice('456789') for i in range(6))
        self.driver.find_element_by_xpath('//*[@id="Pincode"]').send_keys(pin)

        # Account Details
        self.driver.find_element_by_xpath('//*[@id="Bank"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').click()
        self.driver.find_element_by_xpath('//*[@id="BankIFSCCode"]').send_keys('SBIN0070192')
        self.driver.find_element_by_xpath('//*[@id="ifscButton1"]').click()

        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').click()
        accno = ''.join(random.choice('0123456789') for i in range(14))
        self.driver.find_element_by_xpath('//*[@id="BankAccountNo"]').send_keys(accno)

        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').click()
        self.driver.find_element_by_xpath('//*[@id="txtAccountHoldersName"]').send_keys('Sumona')

        self.driver.find_element_by_xpath('//*[@id="btnVerify"]').click()

        # Submit
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/button[1]').click()
        time.sleep(5)
        self.driver.switch_to.alert.accept()

        time.sleep(5)
        time.sleep(5)
        self.driver.switch_to.alert.accept()
        time.sleep(5)

        element = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/h5')
        time.sleep(5)
        assert element.text == 'The beneficiary application form is sent for approval'
        time.sleep(5)
        time.sleep(5)
    def tearDown(self):
       self.driver.quit()

if __name__ == '__main__':
    unittest.main()
