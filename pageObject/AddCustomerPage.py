import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_selector = "body > div.wrapper > aside > div > div.os-padding > div > div > nav > ul > li:nth-child(4)"
    lnkCustomers_menuitem_selector ="body > div.wrapper > aside > div > div.os-padding > div > div > nav > ul > li.nav-item.has-treeview.menu-open > ul > li:nth-child(1)"
    btnAddnew_selector ="body > div.wrapper > div.content-wrapper > form:nth-child(2) > div > div > a"
    txtEmail_id="Email"
    txtpassword_id="Password"
    txtcustomerRoles_css_selector = "#customer-info > div.card-body > div:nth-child(10) > div.col-md-9 > div > div.input-group > div"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_id = "48a23783-176f-482d-938e-a121adca6081"
    lstitemGuests_selector = "#\34 8a23783-176f-482d-938e-a121adca6081"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.CSS_SELECTOR,self.lnkCustomers_menu_selector).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.CSS_SELECTOR,self.lnkCustomers_menuitem_selector).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.CSS_SELECTOR,self.btnAddnew_selector).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txtpassword_id).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element(By.CSS_SELECTOR,self.txtcustomerRoles_css_selector ).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.ID,self.lstitemRegistered_id)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.ID,self.lstitemRegistered_id).click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_selector)
        #elif role=='Registered':
            #self.listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
        #self.listitem.click()
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        time.sleep(2)
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()