import pytest 
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
  
    baseURL=ReadConfig.getApllicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()
   
   
   
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
            self.logger.info("*****Test_001_Login****")
            self.logger.info("*****Verify Home Page Title****")
            self.driver=setup
            self.driver.get(self.baseURL)
            act_title=self.driver.title
            if act_title=="Your store. Login":
                assert True
                self.driver.close()
                self.logger.info("*****Home Page Title test is passed****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
                self.driver.close()
                self.logger.error("*****Home Page Title test is Failed****")
                assert False

           

    @pytest.mark.regression
    def test_logging(self,setup):
            self.logger.info("*****Verify Loggin****")
            self.driver=setup
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            act_title=self.driver.title
            if act_title=="Dashboard / nopCommerce administration":
                assert True
                self.driver.close()
                self.logger.info("*****Login test is passed****")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+"test_logging.png")
                self.driver.close()
                self.logger.error("*****Login test is failed****")
                assert False  
            


    
   

    
   
        

    
        






    



        


    