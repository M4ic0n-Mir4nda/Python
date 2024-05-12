from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get('http://google.com.br') 
navegador.maximize_window()
print('título:', navegador.title)
print('endereço URL:', navegador.current_url)
print('código fonte:', navegador.page_source[:100])

navegador.close()
