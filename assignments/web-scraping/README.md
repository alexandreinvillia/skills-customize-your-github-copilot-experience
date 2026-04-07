# 📘 Assignment: Web Scraping with Python

## 🎯 Objective

Nesta tarefa, você aprenderá a coletar dados de páginas web usando Python com as bibliotecas `requests` e `BeautifulSoup`. Ao final, você será capaz de extrair, filtrar e salvar informações estruturadas a partir de HTML.

## 📝 Tasks

### 🛠️ Fazer uma Requisição HTTP e Analisar o HTML

#### Description
Use a biblioteca `requests` para buscar o conteúdo HTML de uma URL pública e a biblioteca `BeautifulSoup` para analisá-lo e localizar elementos específicos da página.

#### Requirements
Completed program should:

- Fazer uma requisição GET para uma URL fornecida e verificar se a resposta foi bem-sucedida (status 200)
- Criar um objeto `BeautifulSoup` a partir do conteúdo HTML retornado
- Exibir o título (`<title>`) da página no terminal

Exemplo de saída:
```
Título da página: Example Domain
```

### 🛠️ Extrair e Filtrar Dados da Página

#### Description
Navegue pela estrutura HTML para extrair uma lista de elementos (como links ou parágrafos) e aplique um filtro para exibir apenas os resultados relevantes.

#### Requirements
Completed program should:

- Encontrar todos os links (`<a>`) da página e exibir o texto e a URL de cada um
- Filtrar e exibir apenas os links cujo texto não está vazio
- Contar e imprimir o total de links encontrados após a filtragem

Exemplo de saída:
```
Link: More information... -> https://www.iana.org/domains/reserved
Total de links encontrados: 1
```

### 🛠️ Salvar os Dados Extraídos em um Arquivo CSV

#### Description
Persista os dados coletados salvando-os em um arquivo CSV para que possam ser consultados posteriormente ou usados em análises.

#### Requirements
Completed program should:

- Criar (ou sobrescrever) um arquivo `output.csv` com os dados extraídos
- O arquivo deve conter pelo menos duas colunas: `texto` e `url`
- Cada link filtrado deve corresponder a uma linha no arquivo CSV
- Exibir uma mensagem de confirmação ao final indicando quantos registros foram salvos

Exemplo de saída:
```
2 registros salvos em output.csv
```
