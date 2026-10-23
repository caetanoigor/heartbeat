# 🫀 Heartbeat

API REST desenvolvida em FastAPI para monitoramento, diagnóstico e telemetria de recursos do sistema Linux (CPU, memória RAM e armazenamento em disco), empacotada de forma leve e segura através de containers Podman.

---

## 📌 Visão Geral

O **Heartbeat** foi concebido com uma arquitetura modular que separa a camada de coleta direta de hardware da camada de transporte HTTP. Permite a integração simples com ferramentas externas de observabilidade, painéis de controle ou rotinas automatizadas de *health check*.

### Principais Características
- **Arquitetura Desacoplada**: Separação estrita entre o coletor de telemetria (`app/collector.py`) e a interface web (`app/main.py`).
- **Coleta Precisa**: Medição de CPU com amostragem delta, diferenciação de núcleos lógicos/físicos e conversão precisa em base binária para MB e GB.
- **Containerização Segura**: Configuração focada no Podman (compatível com Docker), sem privilégios de root (*rootless*) e sem daemon central.
- **Suíte de Testes Integrada**: Validação automatizada das rotas com `pytest` e simulação HTTP em memória com o `TestClient`.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.12+
- **Framework Web**: FastAPI
- **Servidor ASGI**: Uvicorn
- **Extração de Métricas**: psutil
- **Testes Automatizados**: pytest & httpx
- **Containerização**: Podman

---

## 📂 Estrutura do Projeto

heartbeat/
    app/
        __init__.py
        collector.py
        main.py
    tests/
        __init__.py
        test_api.py
    .gitignore
    Containerfile
    README.md
    requirements.txt

---

## 📋 Endpoints da API

| Método | Endpoint | Descrição | Código HTTP |
| :--- | :--- | :--- | :--- |
| GET | `/` | Health check básico de disponibilidade | 200 OK |
| GET | `/metrics` | Retorna o consumo em tempo real de CPU, RAM e disco em JSON | 200 OK |
| GET | `/docs` | Documentação interativa Swagger UI | 200 OK |
| GET | `/redoc` | Documentação técnica alternativa ReDoc | 200 OK |

---

## 📊 Exemplo de Resposta (GET /metrics)

```json
{
  "cpu": {
    "usage_percent": 12.4,
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

## 🚀 Como Executar
Opção 1: Execução com Container (Podman)

Construir a imagem local:
podman build -t heartbeat:latest .

Iniciar o container em segundo plano:
podman run -d --name heartbeat-app -p 8000:8000 heartbeat:latest

Acessar as rotas no navegador:

Métricas: http://localhost:8000/metrics

Documentação Swagger: http://localhost:8000/docs

Parar e remover o container:
podman stop heartbeat-app
podman rm heartbeat-app

Opção 2: Execução Direta no Sistema (Local)

Criar e ativar o ambiente virtual:
python -m venv venv
source venv/bin/activate

Instalar as dependências:
pip install -r requirements.txt

Executar os testes automatizados:
pytest -v

Iniciar o servidor de desenvolvimento:
uvicorn app.main:app --reload --port 8000