from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time

from pageobjects.CheckoutPage import CheckoutPage
from pageobjects.HomePage import HomePage
from pageobjects.PurchasePage import PurchasePage
from utilities.BassClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.get('https://rahulshettyacademy.com/angularpractice/')

        log = self.test_loggingDemo()

        self.driver.implicitly_wait(5)
        homePage = HomePage(self.driver)
        checkout = homePage.shopItems()
        #self.driver.find_element(By.LINK_TEXT, 'Shop').click()


        products = checkout.getProducts()
        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        count = -1
        for product in products:
            count = count + 1
            productName = product.text

            if productName == 'Blackberry':
                #product.find_element(By.XPATH, 'div//button').click()
                checkout.addProduct()[count].click()

        #self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkout.checkoutButton().click()

        #self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-success')]").click()
        purchasePage = checkout.confirmPage()

        #purchase = PurchasePage(self.driver)
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        purchasePage.enterCountry().send_keys("ind")
        self.verifyLinkPresnce("India")

        #self.driver.find_element(By.LINK_TEXT, 'India').click()
        purchasePage.addCountry().click()

        #self.driver.find_element(By.XPATH, "//div[contains(@class, 'checkbox-primary')]").click()
        purchasePage.clickCheckbox().click()

        #self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
        purchasePage.confirmPurchase().click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText
