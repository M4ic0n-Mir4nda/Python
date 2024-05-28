import os
from pytest import fixture
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@fixture
def form_aluno():
    chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    pasta = os.path.dirname(os.path.realpath(__file__))
    local_path = f'file://{pasta}/../app/template/'
    chrome.get(f'{local_path}aluno.html')
    yield chrome
    chrome.close()