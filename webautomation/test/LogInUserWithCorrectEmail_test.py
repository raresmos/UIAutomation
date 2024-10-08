from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webautomation.source.helpers.UserInputLocators import TestBroswerHelper
from webautomation.source.helpers.UserInputLocators import TestClickSingUp
from webautomation.source.helpers.UserInputLocators import TestInputUserDetails
from webautomation.source.helpers.UserInputLocators import TestDeleteAccount
from webautomation.source.helpers.UserInputLocators import TestContinueButton


class TestLogInWithCorrectEmail():
    def __init__(self):
        self.url = "https://www.automationexercise.com/"
        self.broswer_helper = TestBroswerHelper(self.url)

    def test_LunchBroser(self):
        self.driver = self.broswer_helper.test_lunch_broswer()

    def test_HomePageCheck(self):
        try:
            home_page_text = self.driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[1]/div[1]/a[1]/button")
            home_page_text = home_page_text.text
            if home_page_text == "Test Cases":
                print("Home page is visible")

            else:
                print("Home page is not visible")
        except Exception as e:
            print(f"Error while checking the home page: {e}")


    def test_PerformSingUp(self):
        click_singup = TestClickSingUp(self.driver)
        click_singup.test_click_singup()

    def test_CheckSingUpPage(self):
        try:
            expected_text = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located(((By.XPATH,"//*[contains(text(),'Login to your account')]"))))
            if expected_text.text == "Login to your account":
                print('LogIn page is visible')
                return True
            else:
                print("Login page is not visible")
                return False

        except Exception as e:
            print(f"Error while checking LogIn page: {e}")
            return False

    def test_InputUserDetails(self, email, password):
        input_details = TestInputUserDetails(self.driver)
        input_details.test_input_details(email, password)

    def test_CheckIflogedIn(self):
        try:
            message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a")))
            if message.text == "Logged in as rares":
                print('You are logged in!')
                return True
        except Exception as e:
            print(f'Error while checking id you are logged in: {e}')
            return False

    def test_DeleteAccount(self):
        delete = TestDeleteAccount(self.driver)
        delete.test_click_deletebutton()

        try:
            message = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div/h2/b")))
            if message.text == "ACCOUNT DELETED!":
                print('Account was deleted successfully!')
                return True
            else:
                print('Account deleted text is not present')
                return False
        except Exception as e:
            print(f'Error while checking if the account was deleted: {e} ')
            return False

    def test_CountinueButton(self):
        button = TestContinueButton(self.driver)
        button.test_click_continue()

    def test_CloseBroswer(self):
        if self.broswer_helper.driver:
            self.broswer_helper.driver.quit()
            print("The test was successfully done without any errors!")

automation = TestLogInWithCorrectEmail()
automation.test_LunchBroser()
automation.test_HomePageCheck()
automation.test_PerformSingUp()
automation.test_CheckSingUpPage()
email = "refsmgfosddbbb@gmail.com"
password = "12345"
automation.test_InputUserDetails(email, password)
automation.test_CheckIflogedIn()
automation.test_DeleteAccount()
automation.test_CountinueButton()
automation.test_CloseBroswer()







