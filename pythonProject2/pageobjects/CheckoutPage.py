from selenium.webdriver.common.by import By

from pageobjects.PurchasePage import PurchasePage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']//div//h4/a")
    add = (By.XPATH, "//div[@class='card h-100']//div//button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirm = (By.XPATH, "//button[@class= 'btn btn-success']")

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def addProduct(self):
        return  self.driver.find_elements(*CheckoutPage.add)

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def confirmPage(self):
        self.driver.find_element(*CheckoutPage.confirm).click()
        purchasePage = PurchasePage(self.driver)
        return purchasePage


