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
driver.get("https://www.facebook.com/")

bt_create_new_acc = driver.find_element(By.XPATH, "//a[text()='Criar nova conta']")
bt_create_new_acc.click()

first_name = driver.find_element(By.NAME, "firstname")
first_name.send_keys('José')

last_name = driver.find_element(By.NAME, "lastname")
last_name.send_keys('Silva')

email = driver.find_element(By.NAME, "reg_email__")
email.send_keys('ze@email.com')

email_conf = driver.find_element(By.NAME, "reg_email_confirmation__")
email_conf.send_keys('ze@email.com')

passwd = driver.find_element(By.NAME, "reg_passwd__")
passwd.send_keys('1234')

month = driver.find_element(By.ID, "month")
sel = Select(month)
sel.select_by_index(11)

day = driver.find_element(By.ID, "day")
sel = Select(day)
sel.select_by_index(11)

year = driver.find_element(By.ID, "year")
sel = Select(year)
sel.select_by_value('2001')


sex_male = driver.find_element(By.XPATH, "//label[text()='Masculino']")
sex_male.click()

botao_sign_up = driver.find_element(By.XPATH, "//button[text()='Cadastre-se']")
botao_sign_up.click()

time.sleep(25)
error_msg = driver.find_element(By.ID, "reg_error_inner")
print(error_msg.text)
