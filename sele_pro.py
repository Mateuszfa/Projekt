from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from test_Data import *



class SwaglabshopAction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)





    def testUsernameIsLocked(self):
        usr_input = self.driver.find_element(By.ID, "user-name")
        usr_input.send_keys(username_bad)
        sleep(1)

        pas_input = self.driver.find_element(By.ID, "password")
        pas_input.send_keys(password)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()
        sleep(2)

        errors = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertEqual(error_text, errors.text)

    def testNoNameEntered(self):

        pas_input = self.driver.find_element(By.ID, "password")
        pas_input.send_keys(password)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()
        sleep(2)

        errors = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertEqual(error_text3, errors.text)
        print("Correct Message")


    def testNoPasswordEntered(self):
        usr_input = self.driver.find_element(By.ID, "user-name")
        usr_input.send_keys(username_good)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()
        sleep(2)

        errors = self.driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.assertEqual(error_text4, errors.text)
        print("Correct Message")


    def testPurchaseOk(self):
        usr_input = self.driver.find_element(By.ID, "user-name")
        usr_input.send_keys(username_good)
        sleep(1)

        pas_input = self.driver.find_element(By.ID, "password")
        pas_input.send_keys(password)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()

        add_item1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_item1.click()
        sleep(1)

        add_item2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item2.click()
        sleep(1)

        add_item3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        add_item3.click()
        sleep(1)

        my_purches = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        my_purches.click()


        my_purches = self.driver.find_element(By.ID, "checkout")
        my_purches.click()
        sleep(1)

        login = self.driver.find_element(By.NAME, "firstName")
        login.send_keys(first_name)
        sleep(1)

        login = self.driver.find_element(By.NAME, "lastName")
        login.send_keys(last_name)
        sleep(1)

        login = self.driver.find_element(By.NAME, "postalCode")
        login.send_keys(zip_code)
        sleep(1)

        login = self.driver.find_element(By.ID, "continue")
        login.click()
        sleep(1)

        check_number = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        self.assertEqual("3", check_number.text)
        print("number of item is correct!")

        chech_cash = self.driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
        self.assertEqual(cash, chech_cash.text)

        login = self.driver.find_element(By.NAME, "finish")
        login.click()
        sleep(1)

    def testPurchaseBug1(self):
        usr_input = self.driver.find_element(By.ID, "user-name")
        usr_input.send_keys(username_bug)
        sleep(1)

        pas_input = self.driver.find_element(By.ID, "password")
        pas_input.send_keys(password)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()
        sleep(1)

        add_item1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_item1.click()
        sleep(1)

        add_item2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        add_item2.click()
        sleep(1)

        add_item3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_item3.click()
        sleep(1)

        add_item4 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item4.click()
        sleep(1)

        add_item5 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        add_item5.click()
        sleep(1)

        add_item6 = self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
        add_item6.click()
        sleep(1)

        check_cart = self.driver.find_element(By.ID, "shopping_cart_container")
        check_cart.click()
        sleep(1)

        verified_item = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        verified_item.get_attribute("value")
        self.assertNotEqual(6, verified_item.text)
        print("There should be 6 items in the basket and we have ", verified_item.text)
        sleep(1)

        clear_item = self.driver.find_element(By.ID, "react-burger-menu-btn")
        clear_item.click()
        sleep(1)

        reset_item = self.driver.find_element(By.ID, "reset_sidebar_link")
        reset_item.click()
        sleep(1)

        clear_item = self.driver.find_element(By.ID, "continue-shopping")
        clear_item.click()
        sleep(1)

        check_cart = self.driver.find_element(By.ID, "shopping_cart_container")
        check_cart.click()
        sleep(1)

        verified_item = self.driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
        verified_item.get_attribute("value")
        self.assertEqual("", verified_item.text)
        sleep(1)

        shop_exit = self.driver.find_element(By.ID, "react-burger-menu-btn")
        shop_exit.click()
        sleep(1)

        shop_logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        shop_logout.click()
        sleep(1)



        print("store is buggy, you can't add some item to your cart !!")






    def testPurchaseBug2(self):

        usr_input = self.driver.find_element(By.ID, "user-name")
        usr_input.send_keys(username_bug)
        sleep(1)

        pas_input = self.driver.find_element(By.ID, "password")
        pas_input.send_keys(password)
        sleep(1)

        log_button = self.driver.find_element(By.ID, "login-button")
        log_button.click()
        sleep(1)

        add_item1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_item1.click()
        sleep(1)


        add_item3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_item3.click()
        sleep(1)

        add_item4 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_item4.click()
        sleep(1)

        check_cart = self.driver.find_element(By.ID, "shopping_cart_container")
        check_cart.click()
        sleep(1)


        check_number = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        check_number.get_attribute('values')
        self.assertEqual(check_number.text, '3')
        print("quantity in basket: correct !")


        my_purches = self.driver.find_element(By.ID, "checkout")
        my_purches.click()
        sleep(1)

        login = self.driver.find_element(By.NAME, "firstName")
        login.send_keys(first_name)
        sleep(1)

        login = self.driver.find_element(By.NAME, "lastName")
        login.send_keys(last_name)
        sleep(1)

        login = self.driver.find_element(By.NAME, "postalCode")
        login.send_keys(zip_code)
        sleep(1)

        login = self.driver.find_element(By.ID, "continue")
        login.click()

        error = self.driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')
        self.assertEqual(error_text2,error.text)


        check_fname = self.driver.find_element(By.ID, "first-name",)
        test1 = check_fname.get_attribute("value")
        self.assertNotEqual(first_name,test1)
        print("pole First name ",test1)
        sleep(1)


        check_lname = self.driver.find_element(By.ID, "last-name")
        test2 = check_lname.get_attribute("value")
        self.assertNotEqual(last_name,test2)
        print("pole last name ",test2)
        sleep(1)


        check_pcode = self.driver.find_element(By.ID, "postal-code")
        test3 = check_pcode.get_attribute("value")
        self.assertEqual(zip_code,test3)
        print("pole zip Code ",test3)
        sleep(1)


        back_click = self.driver.find_element(By.NAME, "cancel")
        back_click.click()
        sleep(1)

        re_item = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        re_item.click()

        re_item = self.driver.find_element(By.ID, "remove-sauce-labs-onesie")
        re_item.click()

        re_item = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")
        re_item.click()


        shop_exit = self.driver.find_element(By.ID, "react-burger-menu-btn")
        shop_exit.click()
        sleep(1)


        shop_logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        shop_logout.click()
        sleep(1)

        print("store is buggy, you can't make a purchase !!" )



    def tearDown(self):
        self.driver.quit()
