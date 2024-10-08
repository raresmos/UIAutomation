import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webautomation.source.helpers.UserInputLocators import TestBroswerHelper
from webautomation.source.helpers.UserInputLocators import TestUserInputFields
from webautomation.source.helpers.UserInputLocators import TestInputCardDetails
from webautomation.source.helpers.UserInputLocators import TestDeleteAccount
from webautomation.source.helpers.UserInputLocators import TestContinueButton


class TestPlaceOrderCheckOut():
    def __init__(self):
        self.url = "https://www.automationexercise.com/"
        self.broswer_helper = TestBroswerHelper(self.url)

    def test_LunchBroswer(self):
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

    def test_add_product_in_cart(self):
        product = self.driver.find_element(By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/img")
        self.driver.execute_script("arguments[0].scrollIntoView();", product)
        add_to_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-default.add-to-cart")))

        action = ActionChains(self.driver)
        action.move_to_element(add_to_cart).click().perform()
        print('The product was added in the cart')

        view_cart = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section[2]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/p[2]/a/u")))
        view_cart.click()




    def test_cart_button(self):
        self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
        print("The cart button passed!")

        check_cart_page = self.driver.find_element(By.XPATH, "/html/body/section/div/div[2]/table/thead/tr/td[1]")
        try:
            if check_cart_page.text == "Item":
                print("The cart page is visible")
                return True
            else:
                print("Cart page is not visible")
                return False
        except Exception as e:
            print(f"Error while checking the cart page: {e}")
            return False

    def test_procees_checkout(self):
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.check_out").click()
        print("Proceed button passed")

        register_login = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/section/div/section/div[2]/div/div/div[2]/p[2]/a/u")))
        register_login.click()

    def test_input_new_user(self):

        self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]").send_keys('rares')
        self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]").send_keys('refsmgfosddbbb@gmail.com')
        self.driver.find_element(By.XPATH,"/html/body/section/div/div/div[3]/div/form/button").click()
        print("New User Sing Up fields passed!")

    def TestUserInputFields(self):
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
        print("Continue button passed")

    def test_cart_button(self):
        self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()
        print('Cart button passed')

    def test_proceed_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/section/div/section/div[1]/div/div/a").click()
        print('Proceed to checkout passed')


    def test_checking_order_details(self):

        address_details = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/h2")))
        review_order = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[4]/h2")))
        try:
            if address_details.text.strip() == "Address Details" and review_order.text.strip() == "Review Your Order":
                print("Order details are visible")
                return True
            else:
                print("Order details are not visible")
                return False
        except Exception as e:
            print(f"Error while checking the order details: {e}")
            return False

    def test_input_order_details(self):
        input_order_details = self.driver.find_element(By.CLASS_NAME, "form-control")
        input_order_details.send_keys("Thanks for the order")
        print("Order comments added successfully")

    def test_place_order(self):
        self.driver.find_element(By.CLASS_NAME, "btn.btn-default.check_out").click()
        print("Place Order button passed")

    def test_payment_page(self):
        payment_page_check = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div[2]/h2")))
        try:
            if payment_page_check.text == "Payment":
                print("Payment page is visible")
                return True
            else:
                print("Payment page is not visible")
                return False
        except Exception as e:
            print(f"Error while checking the payment page: {e}")
            return False

    def TestInputCardDetails(self):
        TestInputCardDetails(self.driver).input_card_details()
        print("Card details successfully placed")

    def test_pay_order(self):
        self.driver.find_element(By.ID, "submit").click()
        print("Pay button passed")

    def test_check_if_order_placed(self):
        text = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/h2/b")
        continue_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary")

        try:
            if text.text.strip() == "ORDER PLACED!":
                continue_button.click()
                return True
            else:
                print("Your order was not placed")

        except Exception as e:
            print(f"Error while checking if the order was placed: {e}")
            return False
        print("Place order successfully passed!")

    def test_DeleteAccount(self):
        delete = TestDeleteAccount(self.driver)
        delete.test_click_deletebutton()

        try:
            message = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/section/div/div/div/h2/b")))
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







automation = TestPlaceOrderCheckOut()
automation.test_LunchBroswer()
automation.test_HomePageCheck()
automation.test_add_product_in_cart()
time.sleep(2)
automation.test_cart_button()
automation.test_procees_checkout()
automation.test_input_new_user()
automation.TestUserInputFields()
automation.test_check_if_user_created()
time.sleep(4)
automation.test_click_continue_button()
automation.test_cart_button()
automation.test_proceed_checkout()
automation.test_checking_order_details()
automation.test_input_order_details()
automation.test_place_order()
automation.test_payment_page()
automation.TestInputCardDetails()
automation.test_pay_order()
automation.test_check_if_order_placed()
automation.test_DeleteAccount()
automation.test_CountinueButton()

automation.test_CloseBroswer()
