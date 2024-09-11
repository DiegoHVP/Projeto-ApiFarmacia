from fastapi import FastAPI
from endpoints import farmaceutico, medicamento, fornecedor, cliente, farmacia, compra
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import os


app = FastAPI(title='ModelFarma - Projeto Modelo de Farmacia')

# Configurar as origens permitidas
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Adicionar middleware CORS à aplicação
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)


app.include_router(medicamento.router, tags=['Medicamentos'])
app.include_router(fornecedor.router, tags=["Fornecedores"])
app.include_router(cliente.router, tags=["Clientes"])
app.include_router(farmaceutico.router, tags=["Farmaceuticos"])
app.include_router(farmacia.router, tags=["Farmacias"])
app.include_router(compra.router, tags=["Compras"])

if __name__ == "__main__":
    from uvicorn import run
    run("main:app", host="0.0.0.0", port=8000, reload=True, log_level="info")
