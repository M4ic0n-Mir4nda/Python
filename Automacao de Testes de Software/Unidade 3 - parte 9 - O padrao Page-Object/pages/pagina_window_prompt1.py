from selenium.webdriver.common.by import By

class PaginaWindowPrompt:
    URL = 'https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt'

    def __init__(self, navegador):
        self.navegador = navegador

    def carregar(self):
        self.navegador.get(self.URL)

    def trocar_frame(self):
        self.navegador.switch_to.frame('iframeResult')

    def clicar_no_botao_try_it(self):
        self.navegador.find_element(By.XPATH, "//button['Try it']").click()

    def clicar_no_botao_ok(self):
        self.navegador.switch_to.alert.accept()

    def obter_texto_resultado(self):
        return self.navegador.find_element(By.ID, 'demo').text