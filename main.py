from fastapi import FastAPI
from endpoints import medicamento, fornecedor, cliente, funcionario, farmacia, compra

app = FastAPI()

app.include_router(medicamento.router)
app.include_router(fornecedor.router)
app.include_router(cliente.router)
app.include_router(funcionario.router)
app.include_router(farmacia.router)
app.include_router(compra.router)

if __name__ == "__main__":
    from uvicorn import run
    run("main:app", host="0.0.0.0", port=8000,  reload=True)
