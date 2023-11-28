import re
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class RailWay(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("C:/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://railwayb1.somee.com")
    def test_1_successlogin(self):
        self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[8]/a').click()
        self.username_input= self.driver.find_element_by_id("username")
        username = "thanhle@logigear.com"
        self.username_input.send_keys(username)
        self.password = self.driver.find_element_by_id("password")
        self.password.send_keys("12345678")
        element = self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input')
        element.click()
        welcome_message = self.driver.find_element_by_xpath("//*[contains(text(),'Welcome to Safe Railway')]").text
        expected_message = f"Welcome to '{username}'"
        self.assertEqual(expected_message,welcome_message)
        #if expected_message in welcome_message and username == username_from_message:
         #  print(f"User '{username}' is logged in. Welcome message is displayed.")
        #else:
         #   print("User is not logged in or welcome message is not displayed correctly.")
        #print(expected_message)
    def test_2_usernamblank(self):
        self.username = self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[8]/a').click()
        self.password = self.driver.find_element_by_id("password")
        self.password.send_keys("12345678")
        self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input').click()
        actual_text = self.driver.find_element_by_xpath('//*[@id="content"]/p').text
        expected_message = "There was a problem with your login and/or errors exist in your form."
        self.assertEqual(expected_message, actual_text)
    def test_3_invalidpassword(self):
        self.username = self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[8]/a').click()
        self.username = self.driver.find_element_by_id("username")
        self.username.send_keys("thanhle@logigear.com")
        self.password = self.driver.find_element_by_id("password")
        self.password.send_keys("123456")
        self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input').click()
        actual_text = self.driver.find_element_by_xpath('//*[@id="content"]/p').text
        expected_message = "There was a problem with your login and/or errors exist in your form."
        self.assertEqual(expected_message, actual_text)
    def test_4_navigateloginpage(self):
        self.bookticket = self.driver.find_element_by_xpath("//*[contains(text(),'Book ticket')]").click()
        loginpage= self.driver.title
        assert re.search("Login", loginpage)
    def test_5_severalpassword(self):
        self.username = self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[8]/a').click()
        username_input = self.driver.find_element_by_id("username")
        username_input.send_keys("thanhle@logigear.com")
        for _ in range(3):
            password_input = self.driver.find_element_by_id("password")
            password_input.send_keys("123")
            login_button = self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input')
            login_button.click()
        actual_text = self.driver.find_element_by_xpath('//*[@id="content"]/p').text
        expected_error_message = "You have used 4 out of 5 login attempts. After all 5 have been used, you will be unable to login for 15 minutes."
        self.assertEqual(actual_text, expected_error_message)
        self.myticket = self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[7]/a').click()
        Myticketpage = self.driver.find_element_by_xpath('//*[@id="content"]/h1').text
        expected_error_message = "Manage ticket"
        self.assertEqual(Myticketpage,expected_error_message)
        print(Myticketpage)
    def test6_check_additional_page(self, button_name: str, expect_page_title: str = '', is_check_click_tab: bool = True):
        tab = self.driver.find_element_by_link_text(button_name)
        print(f"{button_name} tab is displayed:", tab.is_displayed())
        if is_check_click_tab & tab.is_displayed():
            tab.click()
            page_title = self.driver.find_element_by_xpath('//*[@id="content"]/h1').text
            if page_title == expect_page_title:
                print(f"User is directed to the {button_name} page")
            else:
                print(f"User is not directed to the {button_name} page")
    def test_6(self):
        self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[8]/a').click()
        self.username_input = self.driver.find_element_by_id("username").send_keys("thanhle@logigear.com")
        self.password = self.driver.find_element_by_id("password").send_keys("12345678")
        self.driver.find_element_by_xpath('//*[@id="content"]/form/fieldset/p/input').click()
        self.test6_check_additional_page(button_name="My ticket", expect_page_title="Manage ticket", is_check_click_tab=True)
        self.test6_check_additional_page(button_name="Change password", expect_page_title="Change password",is_check_click_tab=True)
        self.test6_check_additional_page(button_name="Log out", is_check_click_tab=False)
    def test7(self):
        self.driver.find_element_by_xpath('//*[@id="menu"]/ul/li[7]/a').click()
        self.driver.find_element_by_id("email").send_keys("ni@gmail.com")
        self.driver.find_element_by_id("password").send_keys("Bachni1002@")
        self.driver.find_element_by_id("confirmPassword").send_keys()
