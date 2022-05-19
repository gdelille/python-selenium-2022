'''
Ejercicio 10:
Construir un test que :
Abra la pagina: https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html
Presione el la opción Autocloseable success message
Verificar que se muestra mensaje
Verificar que mensaje mostrado desaparece después de 5 segundos.
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
# espera del elemento Start Download

locator = (By.ID, 'downloadButton')
close_boton: WebElement = wait.until(EC.visibility_of_element_located(locator))

#preguntar si el botón es desplegado
assert close_boton.is_displayed(), 'pop up is not displayed'

#preguntar si el botón recibe los clics
close_boton: WebElement = wait.until(EC.element_to_be_clickable(locator))
# verificar si se puede cliquear
assert close_boton.is_enabled(), 'pop up is not enable'

# Verificar que aparece el mensaje: Complete
# //*[@id="dialog"]/div[1]



# cerrar
close_boton.click()

# close browser
driver.quit()
