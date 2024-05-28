import pytest
from selenium.webdriver.common.by import By
from pages.pagina_window_prompt import PaginaWindowPrompt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome


@pytest.fixture
def pagina():
    servico = Service(ChromeDriverManager().install())
    navegador = Chrome(service=servico)
    pagina_window_promt = PaginaWindowPrompt(navegador)
    return pagina_window_promt


def test_js_prompt_hello_harry_potter(pagina):
    pagina.carregar()
    pagina.trocar_frame()
    pagina.clicar_no_botao_try_it()
    pagina.clicar_no_botao_ok()
    resultado = pagina.obter_texto_resultado()
    assert 'Hello Harry Potter! How are you today?' == resultado

def test_js_prompt_hello_jose(pagina):
    pagina.carregar()
    pagina.trocar_frame()
    pagina.clicar_no_botao_try_it()
    pagina.clicar_no_botao_ok_com_o_nome('Jose')
    resultado = pagina.obter_texto_resultado()
    assert 'Hello Jose! How are you today?' == resultado