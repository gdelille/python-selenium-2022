"""
EJERCICIO 1:
Ir a la página https://laboratorio.qaminds.com/
Escribir un script que:
Permita buscar un iphone desde la barra de búsqueda
Verificar que devuelve un resultado con una imagen que pertenece a un iphone.
"""

#import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from ..lib.factory.factory_driver import get_driver


get_driver('Firefox')

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
#time.sleep(2) #esperamos 2 segundos #NO ES RECOMENDABLE UTILIZAR TIME.SLEEP
driver.implicitly_wait(10)

# Permita buscar un iphone desde la barra de búsqueda
busqueda: WebElement = driver.find_element(By.NAME, 'search')
assert busqueda.is_displayed(), "<< No se encuentra >>"
busqueda.send_keys('iphone')

busqueda_boton: WebElement = driver.find_element(By.XPATH, "//*[@id='search']//button")
assert busqueda_boton.is_displayed(), "<< Botón no visible >>"
busqueda_boton.click()

# Verificar que devuelve un resultado con una imagen que pertenece a un iPhone
#time.sleep(2) #esperamos 2 segundos  #NO ES RECOMENDABLE UTILIZAR TIME.SLEEP
driver.implicitly_wait(10)
iphone = driver.find_element(By.XPATH, "//img[@title='iPhone']")
assert iphone.is_displayed(), "<< iPhone no es visible >>"


# Cerrar navegador
driver.quit()
