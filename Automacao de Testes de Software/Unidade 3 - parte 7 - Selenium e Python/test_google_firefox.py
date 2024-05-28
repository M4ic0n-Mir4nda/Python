from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get('http://google.com.br') 
navegador.maximize_window()
campo_de_busca = navegador.find_element(By.NAME, 'q')
print(campo_de_busca.tag_name)  # textarea