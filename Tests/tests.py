import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class PracticeSoftwareTestingComTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def find_element(self, by, selector, timeout=15):
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, selector))
            )

    def test_title(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")
        self.assertIn("Toolshop", driver.title)

    def test_nav_categories(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nav_categories = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nav_categories.click()

        nav_categories_menu = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')

        self.assertIn("show", nav_categories_menu.get_attribute("class"))
        self.assertIn("show", nav_categories.get_attribute("class"))

    def test_nav_category_hand_tools(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-hand-tools"]')
        ht.click()

        time.sleep(1)

        self.assertIn("Category: Hand Tools",
                      self.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_category_power_tools(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-power-tools"]')
        ht.click()

        time.sleep(1)

        self.assertIn("Category: Power Tools",
                      self.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_category_other(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-other"]')
        ht.click()

        time.sleep(1)

        self.assertIn("Category: Other",
                      self.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_category_special_tools(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-special-tools"]')
        ht.click()

        time.sleep(1)

        self.assertIn("Category: Special Tools",
                      self.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_category_rentals(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        time.sleep(1)

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-rentals"]')
        ht.click()

        time.sleep(1)

        self.assertEqual("Rentals",
                      self.find_element(By.TAG_NAME, 'h1').text)
        
    def test_nav_category_special_tools(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-special-tools"]')
        ht.click()

        time.sleep(1)

        self.assertIn("Category: Special Tools",
                      self.find_element(By.TAG_NAME, 'h2').text)

    def test_nav_contact(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[data-test="nav-contact"]')
        nc.click()

        time.sleep(1)

        self.assertEqual("Contact", self.find_element(
            By.TAG_NAME, 'h3').text)
        
    def test_product_page(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        el = self.find_element(By.ID, 'description')
        self.assertIsNotNone(el)

    def test_product_has_related_products(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        el = self.find_element(By.CLASS_NAME, 'card')
        self.assertIsNotNone(el)

    def test_product_has_img (self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        img = self.find_element(By.CSS_SELECTOR, '.card-img-wrapper > img')
        img.is_displayed()

    def test_product_has_add_to_card_button (self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        img = self.find_element(By.ID, 'btn-add-to-cart')
        img.is_displayed()

    def test_empty_cart (self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/checkout")

        self.assertIn("The cart is empty. Nothing to display.", self.find_element(
            By.TAG_NAME, 'body').text)
        

    def test_site_has_logo (self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com")

        logo = self.find_element(By.CSS_SELECTOR, '.navbar-brand svg')
        assert logo.is_displayed()
    
    def test_nav_sign_in(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[data-test="nav-sign-in"]')
        nc.click()

        time.sleep(1)

        self.assertEqual("Login", self.find_element(By.TAG_NAME, 'h3').text)

    def test_lang_en(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-en"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("This is a DEMO application", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Sort", el_f.text)
        self.assertIn("Price Range", el_f.text)
        self.assertIn("Search", el_f.text)
        self.assertIn("Filters", el_f.text)
        self.assertIn("By category", el_f.text)
        self.assertIn("By brand", el_f.text)

        el_nav = self.find_element(By.ID, 'navbarSupportedContent')

        self.assertIn("Home", el_nav.text)
        self.assertIn("Categories", el_nav.text)
        self.assertIn("Contact", el_nav.text)
        self.assertIn("Sign in", el_nav.text)
        self.assertIn("EN", el_nav.text)

    def test_lang_de(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-de"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Das ist eine Demo Applikation", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Sortieren", el_f.text)
        self.assertIn("Preisspanne", el_f.text)
        self.assertIn("Suche", el_f.text)
        self.assertIn("Filter", el_f.text)
        self.assertIn("Nach Kategorie", el_f.text)
        self.assertIn("Nach Marken", el_f.text)

        el_nav = self.find_element(By.ID, 'navbarSupportedContent')

        self.assertIn("Home", el_nav.text)
        self.assertIn("Kategorien", el_nav.text)
        self.assertIn("Kontakt", el_nav.text)
        self.assertIn("Einloggen", el_nav.text)
        self.assertIn("DE", el_nav.text)

    def test_lang_es(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-es"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Esta es una aplicación DEMO", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Ordenar", el_f.text)
        self.assertIn("Rango de precios", el_f.text)
        self.assertIn("Buscar", el_f.text)
        self.assertIn("Filtros", el_f.text)
        self.assertIn("Por categoría", el_f.text)
        self.assertIn("Por marca", el_f.text)


        el_nav = self.find_element(By.ID, 'navbarSupportedContent')
        
        self.assertIn("Inicio", el_nav.text)
        self.assertIn("Categorías", el_nav.text)
        self.assertIn("Contacto", el_nav.text)
        self.assertIn("Iniciar sesión", el_nav.text)
        self.assertIn("ES", el_nav.text)


    def test_lang_fr(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-fr"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Ceci est une application de démonstration", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Trier", el_f.text)
        self.assertIn("Fourchette de prix", el_f.text)
        self.assertIn("Rechercher", el_f.text)
        self.assertIn("Filtres", el_f.text)
        self.assertIn("Par catégorie", el_f.text)
        self.assertIn("Par marque", el_f.text)

    def test_lang_nl(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-nl"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Dit is een DEMO-applicatie", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Sorteren", el_f.text)
        self.assertIn("Prijsklasse", el_f.text)
        self.assertIn("Zoeken", el_f.text)
        self.assertIn("Filter", el_f.text)
        self.assertIn("Op categorie", el_f.text)
        self.assertIn("Op merk", el_f.text)

    def test_lang_tr(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-tr"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        self.assertIn("Bu bir DEMO uygulamasıdır", el_c.text)

        el_f = self.find_element(By.ID, 'filters')

        self.assertIn("Sırala", el_f.text)
        self.assertIn("Fiyat Aralığı", el_f.text)
        self.assertIn("Ara", el_f.text)
        self.assertIn("Filtreler", el_f.text)
        self.assertIn("Kategoriye göre", el_f.text)
        self.assertIn("Markaya göre", el_f.text)

    def test_privacy_policy(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[routerlink="privacy"]')
        nc.click()

        time.sleep(1)

        self.assertIn("Privacy Policy for Toolshop", self.find_element(
            By.TAG_NAME, 'body').text)

    def test_contact_empty_form_error(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/contact")

        cs = self.find_element(
            By.CSS_SELECTOR, '[data-test="contact-submit"]')
        cs.click()

        time.sleep(1)

        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="first-name-error"] > div').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="last-name-error"] > div').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="email-error"] > div').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="subject-error"] > div').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="message-error"] > div').is_displayed())

    def test_sign_in_empty_form_error(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/auth/login")

        ls = self.find_element(By.CSS_SELECTOR, '[data-test="login-submit"]')
        ls.click()

        time.sleep(1)

        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="email-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="password-error"]').is_displayed())

    def test_forgot_password_empty_form_error(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/auth/forgot-password")

        fp = self.find_element(
            By.CSS_SELECTOR, '[data-test="forgot-password-submit"]')
        fp.click()

        time.sleep(1)

        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="email-error"]').is_displayed())

    def test_register_empty_form_error(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/auth/register")

        rs = self.find_element(
            By.CSS_SELECTOR, '[data-test="register-submit"]')
        rs.click()

        time.sleep(1)

        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="first-name-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="email-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="dob-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="street-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="postal_code-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="city-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="state-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="country-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="phone-error"]').is_displayed())
        self.assertTrue(self.find_element(By.CSS_SELECTOR,
                        '[data-test="password-error"]').is_displayed())

    def test_search(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("Thor")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(1)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        self.assertIn("Thor", sc.text)

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        self.assertTrue(pn.is_displayed())
        self.assertIn("Thor Hammer", pn.text)

    def test_search_lowercase(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("thor")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(3)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        self.assertIn("thor", sc.text)

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        self.assertTrue(pn.is_displayed())
        self.assertIn("Thor Hammer", pn.text)

    def test_search_uppercase(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("THOR")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(3)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        self.assertIn("THOR", sc.text)

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        self.assertIn("Thor Hammer", pn.text)

    def test_search_with_spaces(self):
        driver = self.driver
        driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("       thor    ")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(2)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        self.assertIn("thor", sc.text)

        # pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        # self.assertIn("Thor Hammer", pn.text)
        
        self.assertIn("There are no products found.", self.find_element(
            By.TAG_NAME, 'body').text)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
