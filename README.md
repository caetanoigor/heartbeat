# Heartbeat

Uma API REST simples em FastAPI para coletar e expor métricas básicas de hardware do sistema Linux (CPU, memória RAM e disco). O projeto já vem pronto para rodar isolado em container com Podman ou diretamente no sistema via virtualenv.

---

## O que o projeto faz

- **Uso de CPU**: monitora a porcentagem média de uso com janela de amostragem curta e identifica a quantidade de núcleos físicos e lógicos.
- **Memória RAM**: calcula a memória total, a quantidade disponível e a porcentagem em uso.
- **Armazenamento**: mede espaço total, livre e ocupado na partição raiz (`/`).
- **Endpoints documentados**: interface Swagger/OpenAPI nativa do FastAPI.
- **Testes unitários**: suíte de validação de rotas com `pytest` e `httpx`.

---

## Tecnologias

- Python 3.12+
- FastAPI & Uvicorn
- psutil
- pytest
- Podman (ou Docker)

---

## Endpoints

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/` | Retorna o status operacional da API |
| GET | `/metrics` | Retorna as métricas de CPU, RAM e disco em JSON |
| GET | `/docs` | Documentação interativa Swagger UI |

---

## Exemplo de retorno (`GET /metrics`)

```json
{
  "cpu": {
    "usage_percent": 14.2,
    "logical_cores": 16,
    "physical_cores": 8
  },
  "memory": {
    "total_mb": 32048,
    "available_mb": 24110,
    "usage_percent": 24.8
  },
  "disk": {
    "total_gb": 476.21,
    "free_gb": 312.85,
    "usage_percent": 34.3
  }
}
```

---

## Como rodar

### 1. Usando Podman (recomendado)

Construa a imagem:
podman build -t heartbeat:latest .


Inicie o container:
podman run -d --name heartbeat-app -p 8000:8000 heartbeat:latest


Acesse no navegador ou via curl:
- `http://localhost:8000/metrics`
- `http://localhost:8000/docs`

Para parar e remover o container:
podman stop heartbeat-app && podman rm heartbeat-app

---

### 2. Rodando localmente

Crie e ative o ambiente virtual:

python3 -m venv venv
source venv/bin/activate


Instale as dependências:
pip install -r requirements.txt


Rode os testes:
pytest -v

Inicie a aplicação:
uvicorn app.main:app --reload --port 8000