from selenium.webdriver.common.by import By
class LoginPage():
    userName_ID = "username"
    password_Xpath = "//input[@id='password']"
    loginButton_Name = "login"
    #logout_LinkText = "Logout"

    def __init__(self,driver):
        self.driver= driver

    def typeUserName(self,userName):
        self.driver.find_element(By.ID, self.userName_ID).send_keys(userName)

    def typePassword(self,password):
        self.driver.find_element(By.XPATH, self.password_Xpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.NAME, self.loginButton_Name).click()

