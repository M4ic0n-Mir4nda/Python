import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


chrome = Chrome(service=ChromeService(ChromeDriverManager().install()))

local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'
chrome.get(f'{local_path}exemplo_click.html')

ancora = chrome.find_element(By.LINK_TEXT, 'Google')

ancora.click()