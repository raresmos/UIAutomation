import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webautomation.source.helpers.UserInputLocators import TestBroswerHelper



class AddReviewOnOrder():

    def __init__(self):
        self.url = "https://www.automationexercise.com/"
        self.broswer_helper = TestBroswerHelper(self.url)

    def test_LunchBroswer(self):
        self.driver = self.broswer_helper.test_lunch_broswer()

    def product_button(self):
        self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[2]/a").click()
        print("Product button passed")

    def check_products_page(self):
        text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/h2")))
        try:
            if text.text == "ALL PRODUCTS":
                print("Text is visible")
                return True
            else:
                print("Text is not visible")
                return False
        except Exception as e:
            print(f"Error while checking the text: {e}")
            return False

    def view_product(self):
        self.driver.find_element(By.XPATH,"/html/body/section[2]/div[1]/div/div[2]/div/div[2]/div/div[2]/ul/li/a").click()
        print("View button passed")


    def check_product_name(self):
        text = WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2")))
        try:
            if text.text == "Blue Top":
                print("Product name is visible")
                return True
            else:
                print("Product name is not visible")
                return False
        except Exception as e:
            print(f"Error while checking the product name: {e}")
            return False

    def user_details_review(self):
        self.driver.find_element(By.ID, "name").send_keys("ionut")
        self.driver.find_element(By.ID, "email").send_keys("ionut@gmail.com")
        self.driver.find_element(By.ID, "review").send_keys("This product is top")
        self.driver.find_element(By.ID, "button-review").click()

        try:
            message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Thank you for your review.' )]")))
            if message.is_displayed():
                print('The review was sent')
                return True
            else:
                print("The review was not sent")
                return False
        except Exception as e:
            print(f"Error while checking the text for review: {e}")




    def test_CloseBroswer(self):
        if self.broswer_helper.driver:
            self.broswer_helper.driver.quit()
            print("The test was successfully done without any errors!")


automation = AddReviewOnOrder()
automation.test_LunchBroswer()
automation.product_button()
automation.check_products_page()
automation.view_product()
automation.check_product_name()
automation.user_details_review()
automation.test_CloseBroswer()