import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
local_path = f'file://{os.path.dirname(os.path.realpath(__file__))}/'
chrome.get(f'{local_path}ex_botao_para_youtube.html')
botao = chrome.find_element(By.TAG_NAME, 'button')
webdriver.ActionChains(chrome).double_click(botao).perform()