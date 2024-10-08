
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webautomation.source.helpers.UserInputLocators import TestUserInputFields



class TestCreateNewUser:
    def __init__(self):
        self.url = 'https://www.automationexercise.com/'
        self.driver = None

    def test_launch_browser(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        accept_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p')
        accept_button.click()

    def test_verify_homepage(self):
        home_page_text = self.driver.find_element(By.XPATH,"/html/body/section[1]/div/div/div/div/div/div[1]/div[1]/a[1]/button")
        home_page_text = home_page_text.text
        if home_page_text == "Test Cases":
            print("Home page is visible")

        else:
            print("Home page is not visible")


    def test_click_singUp(self):
        singUp_button = self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
        singUp_button.click()

        try:
            new_user_details = self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/h2")
            if new_user_details.text == "New User Signup!":
                print("Test passed for singup page")
                return True
            else:
                print("Test Failed for singup page")
        except Exception as e:
            print(f'Error checking singup page: {e}')
            return False

    def test_input_new_user(self):

         self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]").send_keys('rares')
         self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]").send_keys('refsmgfosddbbb@gmail.com')
         self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/button").click()


    def TestCreateUser(self):
        TestUserInputFields(self.driver).test_populate()


    def test_check_if_user_created(self):
        try:
            message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div/h2/b")))
            if message.text == "ACCOUNT CREATED!":
                print('Account was created')
                return True
            else:
                print("Account was not created")
                return False
        except Exception as e:
            print(f'Error verifying account creation: {e}')
            return False

    def test_click_continue_button(self):
        self.driver.find_element(By.XPATH,'/html/body/section/div/div/div/div/a').click()


    def test_close_browser(self):
        # Close the browser
        if self.driver:
            self.driver.quit()


automation = TestCreateNewUser()
try:
    automation.test_launch_browser()
    automation.test_verify_homepage()
    automation.test_click_singUp()
    automation.test_input_new_user()
    automation.TestCreateUser()
    automation.test_check_if_user_created()
    automation.test_close_browser()
except Exception as e:
    print(f"Test failed: {e}")
finally:
    automation.test_close_browser()