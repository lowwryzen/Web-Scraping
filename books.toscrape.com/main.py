from funcs import Web_auto

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import pandas as pd

dados = [
    ["Título", "Preço", "Estoque"]
    ]

site = Web_auto("https://books.toscrape.com/")

livros = site.pegar_infos("class name", "image_container")

while True:
    for indice, livro in enumerate(livros):

        livros = site.pegar_infos("class name", "image_container")
        livro = livros[indice]

        livro.click()

        site.esperar_ate(5)

        titulo = site.pegar_info(By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)").text
        preco = float(site.pegar_info(By.CSS_SELECTOR, ".price_color").text.replace("£", ""))
        estoque = int(site.pegar_info(By.CSS_SELECTOR, ".instock").text.replace("In stock (","").replace(" available)",""))

        dados.append([titulo, preco, estoque])

        site.voltar()

    try:
        botao_proximo = site.pegar_info(By.CSS_SELECTOR, ".next > a:nth-child(1)")
        
        site.executar_script("arguments[0].scrollIntoView();", botao_proximo)
        botao_proximo.click()
    except NoSuchElementException:
        break
    
tabela = pd.DataFrame(dados)
tabela.to_excel("tabela_livros.xlsx")