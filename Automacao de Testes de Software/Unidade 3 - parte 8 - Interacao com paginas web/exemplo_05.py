import os

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
chrome = Chrome(service=servico)
local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'
chrome.get(f'{local_path}pagina_exemplo_05.html')
linguagens = chrome.find_elements(By.NAME,'linguagem')

for linguagem in linguagens:
    if linguagem.get_attribute('value') == 'Python':
        linguagem.click()

for linguagem in linguagens:
    if linguagem.is_selected():
        print(linguagem.get_attribute('value'))