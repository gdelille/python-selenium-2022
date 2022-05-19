'''
Ejercicio 8:
Construir un test que :
Abra la página: https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html
Presione el botón Start Download y espere a que se realice la descarga.
Verificar que aparece el mensaje: Complete!
'''
#
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 10)
driver.maximize_window()

# Abrir página web
driver.get(url)

# Test Logic

# Dar clic en el botón Start Download
start_download = (By.ID, 'downloadButton')
download: WebElement = wait.until(EC.visibility_of_element_located(start_download))
download.click()

#verificar el progreso de la bajada %
progreso = (By.CSS_SELECTOR, '.progress-label') # Sería por XPATH: //*[@class='progress-label']
#Verificar que aparece el mensaje: Complete!
assert wait.until(EC.text_to_be_present_in_element(progreso, 'Complete!')), 'Complete! is not in progress'


# Botón Close
boton_close = (By.XPATH, "//button[text()='Close']")
close_boton: WebElement = wait.until(EC.element_to_be_clickable(boton_close))
assert close_boton.is_enabled(), 'Close button is not enabled'

# cerrar
close_boton.click()

# close browser
driver.quit()
