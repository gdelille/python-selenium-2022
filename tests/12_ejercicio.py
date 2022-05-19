'''
Ejercicio 12
> Implementa la parametrización para el WebDriver
que permita poder ejecutrar los test cases
tanto en Firefox como con Chrome,
y que a su vez cargue configuraciones para modo Incógnito/Private
como Modo Headless y los tiempos de espera para Impricit
y Explicit Wait.

>Construye una suite de test case que realice los tests:
Autocloseable succes message (Selenium Easy)
Start Download
Download

Ejecutar los casos en modo Headless e Incógnito

Los casos de pruebas, deben obtener el mismo resultado
sin importar cómo se realice la ejecución.

'''

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestDownload:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

        # Click download
        download_loc = (By.ID, "downloadButton")
        download: WebElement = self.wait.until(EC.element_to_be_clickable(download_loc))
        download.click()

        # Verify progress label
        progress_label_loc = (By.CLASS_NAME, "progress-label")  # XPATH: //*[@class='progress-label']
        self.wait.until(EC.text_to_be_present_in_element(progress_label_loc, "Complete!"))

        # Verify continue button
        close_btn_local = (By.XPATH, "//button[text()='Close']")
        close_btn: WebElement = self.wait.until(EC.element_to_be_clickable(close_btn_local))
        close_btn.click()

    def test_download_button_2(self):
        """Ejercicio 9"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")

    def test_auto_closable_msg(self):
        """Ejercicio 10"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")

    def teardown_method(self):
        if self.driver:
            self.driver.quit()









