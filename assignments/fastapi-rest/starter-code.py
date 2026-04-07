from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# -------------------------------------------
# Inicialização do servidor FastAPI
# -------------------------------------------

# TODO: Crie uma instância do FastAPI e atribua à variável `app`
app = None  # substitua por FastAPI()


# -------------------------------------------
# Tarefa 1: Endpoint de boas-vindas
# -------------------------------------------

# TODO: Crie um endpoint GET em "/" que retorne:
# {"message": "Bem-vindo à API de Tarefas!"}


# -------------------------------------------
# Tarefa 2: CRUD de Tarefas
# -------------------------------------------

# TODO: Defina o modelo Task usando pydantic.BaseModel
# Campos: id (int), title (str), done (bool)
class Task(BaseModel):
    pass  # substitua pelos campos corretos


# Lista em memória para armazenar as tarefas
tasks: list[Task] = []
next_id = 1  # controle simples de IDs incrementais


# TODO: Crie o endpoint GET /tasks que retorna `tasks`


# TODO: Crie o endpoint POST /tasks que:
#   - Recebe um JSON com o campo "title"
#   - Cria uma nova Task com id=next_id, done=False
#   - Adiciona à lista e retorna a tarefa criada com status 201


# TODO: Crie o endpoint GET /tasks/{task_id} que:
#   - Busca a tarefa pelo id
#   - Retorna a tarefa encontrada
#   - Lança HTTPException(status_code=404) se não encontrada


# TODO: Crie o endpoint DELETE /tasks/{task_id} que:
#   - Remove a tarefa pelo id da lista
#   - Retorna {"message": "Tarefa removida"}
#   - Lança HTTPException(status_code=404) se não encontrada


# -------------------------------------------
# Tarefa 3: Marcar tarefa como concluída
# -------------------------------------------

# TODO: Crie o endpoint PATCH /tasks/{task_id}/done que:
#   - Localiza a tarefa pelo id
#   - Define done=True
#   - Retorna a tarefa atualizada
#   - Lança HTTPException(status_code=404) se não encontrada


# -------------------------------------------
# Executar o servidor (não modifique)
# -------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("starter-code:app", host="0.0.0.0", port=8000, reload=True)
