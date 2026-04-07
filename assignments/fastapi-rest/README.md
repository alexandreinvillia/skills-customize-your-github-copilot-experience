# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Nesta tarefa, você aprenderá a construir uma API REST funcional usando o framework FastAPI em Python. Ao final, você será capaz de criar endpoints HTTP, trabalhar com modelos de dados e retornar respostas JSON estruturadas.

## 📝 Tasks

### 🛠️ Criar o Servidor FastAPI e o Primeiro Endpoint

#### Description
Configure um projeto FastAPI básico, crie o servidor e implemente um endpoint de boas-vindas que retorna uma mensagem JSON ao ser acessado.

#### Requirements
Completed program should:

- Instanciar um objeto `FastAPI` e configurar o servidor com `uvicorn`
- Criar um endpoint `GET /` que retorne um JSON com a chave `message` e uma mensagem de boas-vindas
- O servidor deve estar acessível em `http://localhost:8000`

Exemplo de resposta ao acessar `GET /`:
```json
{"message": "Bem-vindo à API de Tarefas!"}
```

### 🛠️ Implementar um CRUD de Tarefas (To-Do List)

#### Description
Crie um conjunto de endpoints para gerenciar uma lista de tarefas em memória, permitindo criar, listar, buscar e excluir itens.

#### Requirements
Completed program should:

- Definir um modelo `Task` usando `pydantic.BaseModel` com os campos `id` (int), `title` (str) e `done` (bool)
- Implementar `GET /tasks` que retorna a lista completa de tarefas
- Implementar `POST /tasks` que recebe um JSON com `title` e adiciona uma nova tarefa à lista com `done=False`
- Implementar `GET /tasks/{task_id}` que retorna uma única tarefa pelo `id`, retornando HTTP 404 se não encontrada
- Implementar `DELETE /tasks/{task_id}` que remove a tarefa pelo `id`, retornando HTTP 404 se não encontrada

Exemplo de resposta ao acessar `GET /tasks`:
```json
[
  {"id": 1, "title": "Estudar FastAPI", "done": false}
]
```

### 🛠️ Adicionar Atualização de Status da Tarefa

#### Description
Expanda a API adicionando um endpoint para marcar uma tarefa como concluída, praticando o uso do método HTTP PATCH.

#### Requirements
Completed program should:

- Implementar `PATCH /tasks/{task_id}/done` que define `done=True` na tarefa correspondente
- Retornar a tarefa atualizada como resposta com status HTTP 200
- Retornar HTTP 404 caso a tarefa com o `task_id` informado não exista

Exemplo de resposta ao acessar `PATCH /tasks/1/done`:
```json
{"id": 1, "title": "Estudar FastAPI", "done": true}
```
