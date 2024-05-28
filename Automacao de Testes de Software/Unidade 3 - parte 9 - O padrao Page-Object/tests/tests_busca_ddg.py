import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.pagina_busca_dg import PaginaBuscaDDG

@pytest.fixture
def navegador():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    yield navegador
    navegador.close()
    navegador.quit()

def test_busca_site_google(navegador):
    palavras_busca = 'Page Object'
    paginaBusca = PaginaBuscaDDG(navegador)
    paginaBusca.carregar()
    paginaBusca.buscar(palavras_busca)

    assert paginaBusca.conta_resultados() > 0
    assert paginaBusca.conta_palavras_nos_resultados(palavras_busca) > 0
    assert paginaBusca.texto_na_caixa_de_busca() == palavras_busca