from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class Web_auto:
    from selenium.webdriver.common.by import By

    def __init__(self, url:str):
        self.navegador = webdriver.Firefox()
        self.navegador.get(url)

    def __str__(self):
        return self.navegador.title

    def clicar(self, local, nome:str, segundos_espera:int =0):
        """Informe o local do código html e o nome que deseja clicar, e quantos segundos deseja esperar até clicar"""

        self.navegador.implicitly_wait(segundos_espera)
        clique = self.navegador.find_element(local, nome)
        clique.click()

    def pegar_info(self, local, nome:str, segundos_espera:int =0):
        """Pega as informações com base no local do html e o nome, e quantos segundos deseja esperar até carregar"""

        self.navegador.implicitly_wait(segundos_espera)
        info = self.navegador.find_element(local, nome)
        return info

    def pegar_infos(self, local, nome:str, segundos_espera:int = 0):
        """Pega várias informações com base no local do html e o nome, e quantos segundos deseja esperar"""
        self.navegador.implicitly_wait(segundos_espera)
        infos = self.navegador.find_elements(local, nome)
        return infos

    def voltar(self):
        """Volta uma aba do navegador"""

        self.navegador.back()

    def esperar_ate(self, segundos):
        """Espera alguns segundos até acontecer algo"""
        WebDriverWait(self.navegador, segundos)

    def executar_script(self, codigo, elemento):
        """Executa um código em javascript no navegador"""

        self.navegador.execute_script(codigo, elemento)

    def minimizar_janela(self):
        """Minimiza o navegador"""

        self.navegador.minimize_window()

    def maximizar_janela(self):
        """Preenche a tela toda com o navegador"""

        self.navegador.maximize_window()

    def sair_navegador(self):
        """Fecha o navegador"""

        self.navegador.quit()