import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PracticeSoftwareTestingComTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_title(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")
        self.assertIn("Toolshop", driver.title)

    def test_nav_categories(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nav_categories = driver.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nav_categories.click()

        nav_categories_menu = driver.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')

        self.assertIn("show", nav_categories_menu.get_attribute("class"))
        self.assertIn("show", nav_categories.get_attribute("class"))

    def test_nav_category_hand_tools(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = driver.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = driver.find_element(
            By.CSS_SELECTOR, '[data-test="nav-hand-tools"]')
        ht.click()

        self.assertIn("Category: Hand Tools",
                      driver.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_contact(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = driver.find_element(By.CSS_SELECTOR, '[data-test="nav-contact"]')
        nc.click()

        time.sleep(1)

        self.assertEqual("Contact", driver.find_element(
            By.TAG_NAME, 'h3').text)

    def test_nav_sign_in(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = driver.find_element(By.CSS_SELECTOR, '[data-test="nav-sign-in"]')
        nc.click()

        time.sleep(1)

        self.assertEqual("Login", driver.find_element(By.TAG_NAME, 'h3').text)

    def test_lang_en(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        driver.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test="lang-en"]').click()

        time.sleep(1)

        el_c = driver.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("This is a DEMO application", el_c.text)

        el_f = driver.find_element(By.ID, 'filters')

        self.assertIn("Sort", el_f.text)
        self.assertIn("Price Range", el_f.text)
        self.assertIn("Search", el_f.text)
        self.assertIn("Filters", el_f.text)
        self.assertIn("By category", el_f.text)
        self.assertIn("By brand", el_f.text)

        el_nav = driver.find_element(By.ID, 'navbarSupportedContent')

        self.assertIn("Home", el_nav.text)
        self.assertIn("Categories", el_nav.text)
        self.assertIn("Contact", el_nav.text)
        self.assertIn("Sign in", el_nav.text)
        self.assertIn("EN", el_nav.text)

    def test_lang_de(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        driver.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        driver.find_element(By.CSS_SELECTOR, '[data-test="lang-de"]').click()

        time.sleep(1)

        el_c = driver.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Das ist eine Demo Applikation", el_c.text)

        el_f = driver.find_element(By.ID, 'filters')

        self.assertIn("Sortieren", el_f.text)
        self.assertIn("Preisspanne", el_f.text)
        self.assertIn("Suche", el_f.text)
        self.assertIn("Filter", el_f.text)
        self.assertIn("Nach Kategorie", el_f.text)
        self.assertIn("Nach Marken", el_f.text)

        el_nav = driver.find_element(By.ID, 'navbarSupportedContent')

        self.assertIn("Home", el_nav.text)
        self.assertIn("Kategorien", el_nav.text)
        self.assertIn("Kontakt", el_nav.text)
        self.assertIn("Einloggen", el_nav.text)
        self.assertIn("DE", el_nav.text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
