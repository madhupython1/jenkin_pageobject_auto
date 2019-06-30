from selenium import webdriver
class Login:
    def loginto(self):
            global driver
            driver = webdriver.Chrome(
                executable_path="C:/Users/MadhusmitaPanda/PycharmProjects/jenkin_pageobject_auto/drivers/chromedriver.exe")
            # login to application
            driver.get("https://demo.actitime.com/login.do")
            driver.find_element_by_id("username").send_keys("admin")
            driver.find_element_by_name("pwd").send_keys("manager")
            driver.find_element_by_id("loginButton").click()