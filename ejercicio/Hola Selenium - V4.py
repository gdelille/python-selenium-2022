import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = './drivers/chromedriver'
gecko_driver_path = './drivers/geckodriver'

url = 'https://qamindslab.com'

# Ejercicio con el navegador Chrome
#service = Service(chrome_driver_path)

# Ejercicio con el navegador Firefox
service = Service(gecko_driver_path)


# Ejercicio con el navegador de Chrome
# driver = webdriver.Chrome(service=service)
# Ejercicio con el navegador Firefox
driver = webdriver.Firefox(service=service)


driver.get(url)
time.sleep(3)   #espera por 3 
driver.quit()