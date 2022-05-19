"""
EJERCICIO 3:
1. Ir a la página https://laboratorio.qaminds.com/
2. Escribir un script que:
    a. Desde la página principal pueda ir a la sección Login.
    b. Dado un login inválido se muestre un cartel de error con el mensaje:
        "Warning: No match for E-Mail Address and/or Password."
"""

import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
#url = 'https://qamindslab.force.com/s/login/'
url = 'https://laboratorio.qaminds.com/'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.maximize_window()

# Abrir página web
driver.get(url)


# a. Desde la página principal pueda ir a la sección Login.
time.sleep(2) #esperamos 2 segundos
micuenta = driver.find_element(By.LINK_TEST, 'My Account')
assert micuenta.is_displayed(), "<<My Account no está visible>>"
micuenta.click()

time.sleep(1)
login = driver.find_element(By.LINK_TEXT, "Login") 
assert login.is_displayed(), "<<Login no está visible>>"
login.click()

time.sleep(1)
correo = driver.find_element(By.ID, "input-email") 
assert correo.is_displayed(), "<<Correo no está visible>>"
login.click()


# x path selector proporcionado por el profesor para el warning
# //*[contains(@class,'fa-exclamation-circle')]


# Cerrar navegador
driver.quit()
