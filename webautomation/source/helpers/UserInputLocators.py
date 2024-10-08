import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestUserInputFields():

    def __init__(self, driver):
        self.driver = driver

    def test_populate(self):
        try:

            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[1]/div[1]/label/div/span/input").click()
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[4]/input").send_keys('12345')
            Select(self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select")).select_by_visible_text("7")
            Select(self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[5]/div/div[2]/div/select")).select_by_visible_text("January")
            Select(self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select")).select_by_visible_text("1995")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[1]/input").send_keys("Rares")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[2]/input").send_keys("Mos")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[4]/input").send_keys("Placa Real")
            Select(self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[6]/select")).select_by_visible_text("Canada")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[7]/input").send_keys("Barcelona")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/p[8]/input").send_keys("Barcelona")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[9]/input").send_keys("08020")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[10]/input").send_keys("5588899")
            self.driver.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/button").click()

        except Exception as e:
            print(f"Error while populating user input fields: {e}")

class TestBroswerHelper():

    def __init__(self, url):
        self.url = url
        self.driver = None

    def test_lunch_broswer(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        try:

            accept_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p')
            accept_button.click()
            print("Accept cookies clicked")

        except Exception as e:
            print(f"Error while lunching url: {e}")
        return self.driver

class TestClickSingUp():
    def __init__(self, driver):
        self.driver = driver

    def test_click_singup(self):
        sing_up_button = self.driver.find_element(By.CLASS_NAME,"fa.fa-lock")
        sing_up_button.click()

class TestInputUserDetails():
    def __init__(self, driver):
        self.driver = driver

    def test_input_details(self, email_value, password_value):
        email_field = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
        email_field.send_keys(email_value)
        password_field = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
        password_field.send_keys(password_value)
        login_button = self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button")
        login_button.click()

class TestDeleteAccount():
    def __init__(self, driver):
        self.driver = driver

    def test_click_deletebutton(self):
        detele_button = self.driver.find_element(By.XPATH,"/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")
        detele_button.click()

class TestContinueButton():
    def __init__(self, driver):
        self.driver = driver

    def test_click_continue(self):
        self.driver.find_element(By.CLASS_NAME, "btn.btn-primary").click()

class TestInputCardDetails():
    def __init__(self, driver):
        self.driver = driver

    def input_card_details(self):
        self.driver.find_element(By.NAME, "name_on_card").send_keys("Joan Jose")
        self.driver.find_element(By.NAME, "card_number").send_keys("4444444444444444")
        self.driver.find_element(By.CLASS_NAME, "form-control.card-cvc").send_keys("987")
        self.driver.find_element(By.CLASS_NAME, "form-control.card-expiry-month").send_keys("08")
        self.driver.find_element(By.CLASS_NAME, "form-control.card-expiry-year").send_keys("2030")




