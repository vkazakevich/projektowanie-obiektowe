import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestPracticeSoftwareTesting:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def find_element(self, by, selector, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def test_title(self):
        self.driver.get("https://practicesoftwaretesting.com/")
        assert "Toolshop" in self.driver.title

    def test_nav_categories(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nav_categories = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nav_categories.click()

        nav_categories_menu = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')

        assert "show" in nav_categories_menu.get_attribute("class")
        assert "show" in nav_categories.get_attribute("class")

    def test_nav_category_hand_tools(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-hand-tools"]')
        ht.click()

        time.sleep(1)

        assert "Category: Hand Tools" in self.find_element(
            By.TAG_NAME, 'h2').text

    def test_nav_category_power_tools(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-power-tools"]')
        ht.click()

        time.sleep(1)

        assert "Category: Power Tools" in self.find_element(
            By.TAG_NAME, 'h2').text

    def test_nav_category_other(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-other"]')
        ht.click()

        time.sleep(1)

        assert "Category: Other" in self.find_element(By.TAG_NAME, 'h2').text

    def test_nav_category_special_tools(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-special-tools"]')
        ht.click()

        time.sleep(1)

        assert "Category: Special Tools" in self.find_element(
            By.TAG_NAME, 'h2').text

    def test_nav_category_rentals(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        time.sleep(1)

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-rentals"]')
        ht.click()

        time.sleep(1)

        assert "Rentals" == self.find_element(By.TAG_NAME, 'h1').text

    def test_nav_category_special_tools_error(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-categories"]')
        nc.click()

        ht = self.find_element(
            By.CSS_SELECTOR, '[data-test="nav-special-tools"]')
        ht.click()

        time.sleep(1)

        assert "Category: Special Tools" in self.find_element(
            By.TAG_NAME, 'h2').text

    def test_nav_contact(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[data-test="nav-contact"]')
        nc.click()

        time.sleep(1)

        assert "Contact" == self.find_element(By.TAG_NAME, 'h3').text

    def test_product_page(self):
        self.driver.get(
            "https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        el = self.find_element(By.ID, 'description')
        assert el is not None

    def test_product_has_related_products(self):
        self.driver.get(
            "https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        el = self.find_element(By.CLASS_NAME, 'card')
        assert el is not None

    def test_product_has_img(self):
        self.driver.get(
            "https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        img = self.find_element(By.CSS_SELECTOR, '.card-img-wrapper > img')
        assert img.is_displayed()

    def test_product_has_add_to_cart_button(self):
        self.driver.get(
            "https://practicesoftwaretesting.com/product/01JX7PKDNFG1TRMB5696AMH7VR")

        btn = self.find_element(By.ID, 'btn-add-to-cart')
        assert btn.is_displayed()

    def test_empty_cart(self):
        self.driver.get("https://practicesoftwaretesting.com/checkout")

        assert "The cart is empty. Nothing to display." in self.find_element(
            By.TAG_NAME, 'body').text

    def test_site_has_logo(self):
        self.driver.get("https://practicesoftwaretesting.com")

        logo = self.find_element(By.CSS_SELECTOR, '.navbar-brand svg')
        assert logo.is_displayed()

    def test_nav_sign_in(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[data-test="nav-sign-in"]')
        nc.click()

        time.sleep(1)

        assert "Login" == self.find_element(By.TAG_NAME, 'h3').text

    def test_lang_en(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-en"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "This is a DEMO application" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Sort" in el_f.text
        assert "Price Range" in el_f.text
        assert "Search" in el_f.text
        assert "Filters" in el_f.text
        assert "By category" in el_f.text
        assert "By brand" in el_f.text

        el_nav = self.find_element(By.ID, 'navbarSupportedContent')

        assert "Home" in el_nav.text
        assert "Categories" in el_nav.text
        assert "Contact" in el_nav.text
        assert "Sign in" in el_nav.text
        assert "EN" in el_nav.text

    def test_lang_de(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-de"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "Das ist eine Demo Applikation" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Sortieren" in el_f.text
        assert "Preisspanne" in el_f.text
        assert "Suche" in el_f.text
        assert "Filter" in el_f.text
        assert "Nach Kategorie" in el_f.text
        assert "Nach Marken" in el_f.text

        el_nav = self.find_element(By.ID, 'navbarSupportedContent')

        assert "Home" in el_nav.text
        assert "Kategorien" in el_nav.text
        assert "Kontakt" in el_nav.text
        assert "Einloggen" in el_nav.text
        assert "DE" in el_nav.text

    def test_lang_es(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-es"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "Esta es una aplicación DEMO" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Ordenar" in el_f.text
        assert "Rango de precios" in el_f.text
        assert "Buscar" in el_f.text
        assert "Filtros" in el_f.text
        assert "Por categoría" in el_f.text
        assert "Por marca" in el_f.text

        el_nav = self.find_element(By.ID, 'navbarSupportedContent')

        assert "Inicio" in el_nav.text
        assert "Categorías" in el_nav.text
        assert "Contacto" in el_nav.text
        assert "Iniciar sesión" in el_nav.text
        assert "ES" in el_nav.text

    def test_lang_fr(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-fr"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "Ceci est une application de démonstration" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Trier" in el_f.text
        assert "Fourchette de prix" in el_f.text
        assert "Rechercher" in el_f.text
        assert "Filtres" in el_f.text
        assert "Par catégorie" in el_f.text
        assert "Par marque" in el_f.text

    def test_lang_nl(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-nl"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "Dit is een DEMO-applicatie" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Sorteren" in el_f.text
        assert "Prijsklasse" in el_f.text
        assert "Zoeken" in el_f.text
        assert "Filter" in el_f.text
        assert "Op categorie" in el_f.text
        assert "Op merk" in el_f.text

    def test_lang_tr(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        self.find_element(
            By.CSS_SELECTOR, '[data-test="language-select"]').click()
        self.find_element(By.CSS_SELECTOR, '[data-test="lang-tr"]').click()

        time.sleep(1)

        el_c = self.find_element(By.CLASS_NAME, 'container-fluid')
        assert "Bu bir DEMO uygulamasıdır" in el_c.text

        el_f = self.find_element(By.ID, 'filters')

        assert "Sırala" in el_f.text
        assert "Fiyat Aralığı" in el_f.text
        assert "Ara" in el_f.text
        assert "Filtreler" in el_f.text
        assert "Kategoriye göre" in el_f.text
        assert "Markaya göre" in el_f.text

    def test_privacy_policy(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        nc = self.find_element(By.CSS_SELECTOR, '[routerlink="privacy"]')
        nc.click()

        time.sleep(1)

        assert "Privacy Policy for Toolshop" in self.find_element(
            By.TAG_NAME, 'body').text

    def test_contact_empty_form_error(self):
        self.driver.get("https://practicesoftwaretesting.com/contact")

        cs = self.find_element(
            By.CSS_SELECTOR, '[data-test="contact-submit"]')
        cs.click()

        time.sleep(1)

        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="first-name-error"] > div').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="last-name-error"] > div').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="email-error"] > div').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="subject-error"] > div').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="message-error"] > div').is_displayed()

    def test_sign_in_empty_form_error(self):
        self.driver.get("https://practicesoftwaretesting.com/auth/login")

        ls = self.find_element(By.CSS_SELECTOR, '[data-test="login-submit"]')
        ls.click()

        time.sleep(1)

        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="email-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="password-error"]').is_displayed()

    def test_forgot_password_empty_form_error(self):
        self.driver.get(
            "https://practicesoftwaretesting.com/auth/forgot-password")

        fp = self.find_element(
            By.CSS_SELECTOR, '[data-test="forgot-password-submit"]')
        fp.click()

        time.sleep(1)

        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="email-error"]').is_displayed()

    def test_register_empty_form_error(self):
        self.driver.get("https://practicesoftwaretesting.com/auth/register")

        rs = self.find_element(
            By.CSS_SELECTOR, '[data-test="register-submit"]')
        rs.click()

        time.sleep(1)

        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="first-name-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="email-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="dob-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="street-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="postal_code-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="city-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="state-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="country-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="phone-error"]').is_displayed()
        assert self.find_element(
            By.CSS_SELECTOR, '[data-test="password-error"]').is_displayed()

    def test_search(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("Thor")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(1)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        assert "Thor" in sc.text

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        assert pn.is_displayed()
        assert "Thor Hammer" in pn.text

    def test_search_lowercase(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("thor")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(3)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        assert "thor" in sc.text

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        assert pn.is_displayed()
        assert "Thor Hammer" in pn.text

    def test_search_uppercase(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("THOR")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(3)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        assert "THOR" in sc.text

        pn = self.find_element(By.CSS_SELECTOR, '[data-test="product-name"]')
        assert "Thor Hammer" in pn.text

    def test_search_with_spaces(self):
        self.driver.get("https://practicesoftwaretesting.com/")

        sq = self.find_element(By.CSS_SELECTOR, '[data-test="search-query"]')
        sq.send_keys("       thor    ")

        ss = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-submit"]')
        ss.click()

        time.sleep(2)

        sc = self.find_element(
            By.CSS_SELECTOR, '[data-test="search-caption"]')
        assert "thor" in sc.text

        assert "There are no products found." in self.find_element(
            By.TAG_NAME, 'body').text
