from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.pagina_window_prompt import PaginaWindowPrompt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_js_prompt_hello_harry_potter():
    servico = Service(ChromeDriverManager().install())
    navegador = Chrome(service=servico)
    pagina = PaginaWindowPrompt(navegador)
    pagina.carregar()
    pagina.trocar_frame()
    pagina.clicar_no_botao_try_it()
    pagina.clicar_no_botao_ok()
    resultado = pagina.obter_texto_resultado()

    assert 'Hello Harry Potter! How are you today?' == resultado

    navegador.close()
    navegador.quit()