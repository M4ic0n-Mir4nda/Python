import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_busca_site_duckduckgo():
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get('http://www.duckduckgo.com')

    palavras_busca = 'Page Object'

    caixa = navegador.find_element(By.ID, 'searchbox_input')
    caixa.send_keys(palavras_busca)
    caixa.submit()

    time.sleep(5)

    # A etapa de Assert ocorre em três partes neste exemplo. Na primeira parte, o script procura um elemento web com o ID de nome "links", que por sua vez possui um elemento filho div para cada link do resultado. Utiliza-se o buscar por PARTIAL_LINK_TEXT para encontrar todos os resultados da consulta. Note que o método é o find_elements(), com elements no plural, que é um método que devolve uma lista de elementos. Após isso, o script verifica se o tamanho da lista é maior do que zero, ou seja, a consulta trouxe algum resultado.
    links = navegador.find_elements(By.PARTIAL_LINK_TEXT, palavras_busca)
    assert len(links) > 0

    # Embora a consulta tenha trazido alguns links, o script ainda deve verificar se o esse resultado está adequado. Para isso, verifica-se se as palavras submetidas para a consulta encontram-se nos resultados. Pode-se utilizar o XPath para identificar quais são os links resultados que possuem as palavras submetidas nas consultas. Neste trecho do script, o XPath busca uma div com ID igual a "links", então procura por descendentes que contenham as palavras da consulta. Após isso, verifica se o método find_elements() devolveu algum resultado.
    xpath = f"//*[@class='react-results--main']//*[contains(text(), '{palavras_busca}')]"
    resultados = navegador.find_elements(By.XPATH, xpath)
    assert len(resultados) > 0

    # Como na assertion anterior, este trecho do script verifica se pelo menos um resultado foi encontrado. É apenas um teste de sanidade. Poderia ser mais rígido, como por exemplo, verificar se cada link possui as palavras de consulta. Porém nem sempre os resultados trazem as palavras exatamente da mesma forma que foi enviada na consulta. Alguns resultados podem ter letras maiúsculas. Os localizadores e a lógica precisariam ser muito mais complicados para uma verificação avançada.  Logo, uma simples verificação será o suficiente.de texto

    # Por fim, o script verifica se as palavras submetidas para consulta ainda estão na caixa de busca, na página de resultados. Para isso, é necessário buscar novamente o elemento web que representa a caixa de busca, e verificar se o seu conteúdo é igual ao texto utilizado para realizar a busca.
    caixa_de_busca = navegador.find_element(By.ID, 'search_form_input')
    assert caixa_de_busca.get_attribute('value') == palavras_busca

    navegador.close()
    navegador.quit()