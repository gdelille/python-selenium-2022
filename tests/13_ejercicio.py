'''
Ejercicio 13

En la barra de búsqueda, buscar la palabra "Display",
se deberá mostrar un mensaje que no existen productos con la búsqueda.

Luego seleccionar la opción "Search in product descriptions"
y volver a realizar la búsqueda.

La nueva búsqueda deberá mostra 4 resultados de los productos:
Apple Cinema 30", iPod Nano, iPod Touch, MacBook Pro
'''
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config

# Primero idenficar cómo realizar el ejercicio, creando la estructura del mismo
# class TestSearchDisplay:

#     def setup_method(self):
#         # Crear nueva instancia de WebDriver utilizando factory driver
#         self.driver: WebDriver = get_driver()

#         # Crear instancia de WebDriverWait utilizando la información de config.json
#         self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_small())

#         # Abrir la página web
#         self.driver.get(config.get_url())

#     def test(self):
#         pass

#     def teardown_method(self):
#         if self.driver:
#             self.driver.quit()


# Después ir creando el código e ir probando poco a poco
class TestSearchDisplay:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait utilizando la informacion de config.json
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_small())

        # Abrir la pagina web
        self.driver.get(config.get_url())

    def test(self):
        # Search Input
        search_input_loc = (By.NAME, 'search')
        search_input: WebElement = self.wait.until(EC.element_to_be_clickable(search_input_loc))
        search_input.send_keys('Display')

        # Search button
        search_btn_loc = (By.XPATH, "//*[@id='search']//button")
        search_btn: WebElement = self.wait.until(EC.element_to_be_clickable(search_btn_loc))
        search_btn.click()

        # No products msg
        products_msg_loc = (By.XPATH, "//*[@id='button-search']/following-sibling::p")
        no_products_msg = 'There is no product that matches the search criteria.'
        assert self.wait.until(EC.text_to_be_present_in_element(products_msg_loc, no_products_msg))

        # Checkbox
        checkbox_loc = (By.ID, 'description')
        checkbox: WebElement = self.wait.until(EC.element_to_be_clickable(checkbox_loc))
        checkbox.click()
        assert checkbox.is_selected()

        # Search button
        search_desc_btn_loc = (By.ID, 'button-search')
        search_desc_btn: WebElement = self.wait.until(EC.element_to_be_clickable(search_desc_btn_loc))
        search_desc_btn.click()

        for product_name in ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']:
            loc = (By.LINK_TEXT, product_name)
            self.wait.until(EC.element_to_be_clickable(loc))

# Otra opción de búsqueda de los productos -sustituiría las líneas 82, 83, 84-
# Find all products
# products_loc = (By.XPATH, "//*[@class='caption']//a")
# products: list = self.wait.until(EC.visibility_of_all_elements_located(products_loc))
# for product in products:
#     print(product.text)
#     assert product.text in ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

