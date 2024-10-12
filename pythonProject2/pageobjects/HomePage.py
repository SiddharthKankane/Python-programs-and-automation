from selenium.webdriver.common.by import By

from pageobjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.LINK_TEXT, 'Shop')

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckoutPage(self.driver)
        return checkout
