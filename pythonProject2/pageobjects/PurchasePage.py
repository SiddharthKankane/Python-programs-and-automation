from selenium.webdriver.common.by import By


class PurchasePage:
    def __init__(self, driver):
        self.driver =  driver

    country = (By.ID, "country")
    choose = (By.LINK_TEXT, 'India')
    check = (By.XPATH, "//div[contains(@class, 'checkbox-primary')]")
    purchase =(By.CSS_SELECTOR, "input[type='submit']")

    def enterCountry(self):
        return self.driver.find_element(*PurchasePage.country)

    def addCountry(self):
        return self.driver.find_element(*PurchasePage.choose)

    def clickCheckbox(self):
        return self.driver.find_element(*PurchasePage.check)

    def confirmPurchase(self):
        return self.driver.find_element(*PurchasePage.purchase)

