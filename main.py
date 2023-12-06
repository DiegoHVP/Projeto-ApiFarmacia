from fastapi import FastAPI
from endpoints import medicamentos, fornecedores, clientes, funcionarios, farmacias

app = FastAPI()

app.include_router(medicamentos.router)
app.include_router(fornecedores.router)
app.include_router(clientes.router)
app.include_router(funcionarios.router)
app.include_router(farmacias.router)

if __name__ == "__main__":
    from uvicorn import run
    run("main:app", host="0.0.0.0", port=8000,  reload=True)
