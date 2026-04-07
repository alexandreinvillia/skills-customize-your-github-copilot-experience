import requests
from bs4 import BeautifulSoup
import csv

# URL de exemplo para praticar web scraping
URL = "https://example.com"

# -------------------------------------------
# Tarefa 1: Fazer a requisição e analisar o HTML
# -------------------------------------------

# TODO: Use requests.get() para buscar o conteúdo da URL
response = None  # substitua por requests.get(URL)

# TODO: Verifique se a requisição foi bem-sucedida (status_code == 200)

# TODO: Crie um objeto BeautifulSoup com o conteúdo HTML retornado
soup = None  # substitua por BeautifulSoup(...)

# TODO: Exiba o título da página (soup.title.string)


# -------------------------------------------
# Tarefa 2: Extrair e filtrar links da página
# -------------------------------------------

links_filtrados = []

# TODO: Use soup.find_all("a") para encontrar todos os links
# TODO: Para cada link, obtenha o texto e o atributo "href"
# TODO: Filtre apenas os links cujo texto não seja vazio (use .strip())
# TODO: Imprima cada link no formato: "Link: <texto> -> <url>"

# TODO: Imprima o total de links encontrados


# -------------------------------------------
# Tarefa 3: Salvar os dados em um arquivo CSV
# -------------------------------------------

# TODO: Abra (ou crie) o arquivo "output.csv" para escrita
# TODO: Escreva um cabeçalho com as colunas "texto" e "url"
# TODO: Escreva uma linha para cada link em links_filtrados
# TODO: Imprima uma mensagem de confirmação com o total de registros salvos
