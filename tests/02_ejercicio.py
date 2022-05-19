"""
EJERCICIO 2:
Ir a la página https://laboratorio.qaminds.com/
Escribir un script que:
> Seleccione la opción Tablets
> Aparezca un item con titulo: Samsung Galaxy Tab 10.1
> Seleccione dicho item

> Verifique:
    El costo del item es de $241.99
    Puede agregarlo a una Wish List
    Puede agregarlo al Carrito
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
time.sleep(2) #esperamos 2 segundos


#Seleccione la opción Tablets
tablets = driver.find_element(By.LINK_TEXT, 'Tablets')
assert tablets.is_displayed(), "<< No se encuentra Tablets >>"
tablets.ckick()

# Samsung
time.sleep(2) #esperamos 2 segundos
samsung = driver.find_element(By.LINK_TEXT, 'Samsung Galaxy Tab 10.1')
assert samsung.is_displayed(), "<< No se encuentra Samsung Galaxy Tab 10.1>>"
samsung.click()


# Verifique que: el costo del item es de $241.99
time.sleep(2) #esperamos 2 segundos
price = driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/ul[2]/li[1]/h2")
# EL XPARH EN FIREFOX
# /html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/p[2]
#price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/p[2]")
assert price.is_displayed(), "<< No es visible el precio >>"
assert price.text == '$241.99', "<< No es $241.99 el precio >>"

# Verifique que: puede agregarlo a una Wish List
time.sleep(2) #esperamos 2 segundos
wish_list = driver.find_element(By.XPATH, "//button[@data-original-title='Add to Wish List']")
#//*[@id="content"]/div[3]/div/div/div[2]/div[2]/button[1]
# EL XPARH EN FIREFOX
# /html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div[2]/button[2]
#price = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div[2]/button[2]")
assert wish_list.is_displayed(), "<< No es visible la Wish List>>"
wish_list.click()

# Verifique que: puede agregarlo al Carrito
time.sleep(2) #esperamos 2 segundos
car = driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div/div/div[2]/div[2]/button[1]")
assert car.is_displayed(), "<< No es visible el Carrito>>"
car.click()


#/html/body/div[2]/div[2]/div/div[3]/div/div/div[2]/div[2]/button[1]


# Cerrar navegador
driver.quit()
