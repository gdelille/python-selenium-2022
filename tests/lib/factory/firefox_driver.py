'''
Lunes 09 mayo 2022
Editar el archivo ./lib/factory/firefox_driver.py
'''

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver

def create_driver() -> WebDriver:
    # Init Browsers
    ff_options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference("browse.privatebrowser.autostart", True)
    ff_options.headless = True
    driver_path = 'drivers/geckodriver'
    service = Service(driver_path)
    print(f'HEADLESS: {ff_options.headless}')
    return webdriver.Firefox(service=service, options=ff_options, firefox_profile=ff_profile)

