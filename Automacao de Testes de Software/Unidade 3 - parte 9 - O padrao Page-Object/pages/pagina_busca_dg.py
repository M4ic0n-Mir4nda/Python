from selenium.webdriver.common.by import By

class PaginaBuscaDDG:
    URL = 'https://www.duckduckgo.com'

    def __init__(self, navegador):
        self.navegador = navegador

    def carregar(self):
        self.navegador.get(self.URL)

    def buscar(self, palavras_busca):
        caixa = self.navegador.find_element(By.ID, 'searchbox_input')
        caixa.send_keys(palavras_busca)
        caixa.submit()

    def conta_resultados(self):
        xpath = f'//*[@class="react-results--main"]/li'
        links = self.navegador.find_elements(By.XPATH, xpath)
        return len(links)

    def conta_palavras_nos_resultados(self, palavras_busca):
        xpath = f"//*[@class='react-results--main']//*[contains(text(), '{palavras_busca}')]"
        resultados = self.navegador.find_elements(By.XPATH, xpath)
        return len(resultados)

    def texto_na_caixa_de_busca(self):
        caixa_de_busca = self.navegador.find_element(By.ID, 'search_form_input')
        return caixa_de_busca.get_attribute('value')