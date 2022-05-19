"""
EJERCICIO 5:
    Ir a la página https://demoqa.com/select-menu
    Escribir un script que:

    seleccione de la primera lista Old Style Select Menu la opción “green”
    verifique que la opción ha sido seleccionada.
"""

import time
from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


# Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
#url = 'https://qamindslab.force.com/s/login/'
#url = 'https://laboratorio.qaminds.com/'
url = 'https://demoqa.com/select-menu'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)

#driver.maximize_window()

# Abrir página web
driver.get(url)




# Test Logic
time.sleep(2)
colors = driver.find_element(By.ID, "oldSelectMenu")
assert colors.is_displayed(), "Colors is not visible"
colors_dropdown = Select(colors)
colors_dropdown.select_by_visible_text("Green")

selected_option: WebElement = colors_dropdown.first_selected_option  #guardarlo en una variable

assert selected_option.text == 'Green", "Green is not selected"


colors.click()

# Cerrar navegador
time.sleep(2)
driver.quit()