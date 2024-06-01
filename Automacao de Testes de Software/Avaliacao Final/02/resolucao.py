from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

# Acessando a página da música
url = 'https://www.letras.com.br/belo/perfume'
driver.get(url)

time.sleep(5)

# Localizando o elemento que contém a letra da música
try:
    letra_element = driver.find_element(By.CLASS_NAME, 'lyrics-section')
    letra = letra_element.text
    print(f"Perfume:\n{letra}")
except Exception as e:
    print(f"Erro ao obter a letra da música: {e}")

# Fechando o navegador
driver.quit()
