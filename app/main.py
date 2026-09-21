from fastapi import FastAPI
from app.collector import get_system_metrics

app = FastAPI(
    title = 'Heartbeat API',
    description = 'API de telemetria do hardware do sistema.',
    version = '0.1.0'
)

@app.get('/')
def read_root():
    return {
        'service' : 'heartbeat',
        'status' : 'online',
        'docs' : '/docs'
    }
    
@app.get('/metrics')
def read_metrics():
    return get_system_metrics()