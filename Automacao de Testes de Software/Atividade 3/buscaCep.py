import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)
driver.maximize_window()
driver.implicitly_wait(0.5)

driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

input_endereco = driver.find_element(By.ID, "endereco")
input_endereco.send_keys("11000")

button = driver.find_element(By.XPATH, "//button[text()='Buscar']")
button.click()

table = driver.find_element(By.ID, "resultado-DNEC")

endereco = table.find_element(By.XPATH, ".//tbody/tr[1]/td[1]").text
bairro = table.find_element(By.XPATH, ".//tbody/tr[1]/td[2]").text
cidade = table.find_element(By.XPATH, ".//tbody/tr[1]/td[3]").text

time.sleep(10)
print(endereco)
print(bairro)
print(cidade)
