import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'
url = 'https://qamindslab.force.com/s/login/'
#url = 'https://laboratorio.qaminds.com/'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)

driver.maximize_window()

# Abrir página
driver.get(url)


# Buscar input usuario
time.sleep(2)
user: WebElement = driver.find_element(By.XPATH, "//input[@placeholder='Usuario']")
assert user.is_displayed(), "Usuario no es visible"
user.clear()
user.send_keys("luis.rivas.0606@gmail.com")


# Cerrar navegador
driver.quit()
