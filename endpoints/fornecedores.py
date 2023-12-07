import sqlite3
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *

router = APIRouter()

conn = sqlite3.connect("dados_farmacia.db")
cursor = conn.cursor()

# CRUD Fornecedor
# ADD Fornecedores
@router.post("/fornecedores/", status_code=status.HTTP_201_CREATED)
async def create_fornecedor(fornecedor: Fornecedor):
    try:
        query = "INSERT INTO Fornecedores (nome, contato, medicamento_id) VALUES (?, ?, ?)"
        values = (fornecedor.nome, fornecedor.contato, fornecedor.medicamento_id)
        print(values)
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Fornecedor {fornecedor.nome} foi criado com sucesso"}
    except Exception as e:
        return {"error": str(e)}

# LER Fornecedor POR ID
@router.get("/fornecedores/{id}")
async def get_fornecedor(id: int):
    try:
        query = "SELECT * FROM Fornecedores WHERE id = ?"
        cursor.execute(query, (id,))
        dadosOne = cursor.fetchone()
        if not dadosOne:
            raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
        
        fornecedorDados = {
            "id": dadosOne[0],
            "nome": dadosOne[1],
            "contato": dadosOne[2] ,
            "medicamento_id": dadosOne[3]
        }
        
        return {"Fornecedor": fornecedorDados}
    except Exception as e:
        return {"error": str(e)}

# LER TODOS OS Forncedores
@router.get("/fornecedores/")
async def get_fornecedores():
    try:
        query = "SELECT * FROM Fornecedores"
        cursor.execute(query)
        dadosAll = cursor.fetchall()
        if not dadosAll:
            raise HTTPException(status_code=404, detail="Nenhum fornecedor encontrado")
        fornecedoresDados = []
        for dadosOne in dadosAll:
            
            dadosOne = {
                "id": dadosOne[0],
                "nome": dadosOne[1],
                "contato": dadosOne[2],
                "medicamento_id": dadosOne[3]
            }
            fornecedoresDados.append(dadosOne)

        return {"fornecedores": fornecedoresDados}
    except Exception as e:
        return {"error": str(e)}

# ATUALIZAR Fornecedor por ID
@router.put("/fornecedores/{id}")
async def update_fornecedor(id: int, fornecedor: Fornecedor):
    try:
        query_select = "SELECT * FROM Fornecedores WHERE id = ?"
        cursor.execute(query_select, (id,))
        fornecedorAntigo = cursor.fetchone()
        NomeFornecedorAntigo = fornecedorAntigo[1] #PEGA NOME

        query = "UPDATE Fornecedores SET nome=?, contato=? WHERE id=?"
        values = (fornecedor.nome, fornecedor.contato, id)
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Fornecedor {NomeFornecedorAntigo} foi atualizado"}
    except Exception as e:
        return {"error": str(e)}

# DELETAR Fornecedor POR ID
@router.delete("/fornecedores/{id}")
async def delete_fornecedor(id: int):
    try:
        query_select = "SELECT * FROM Fornecedores WHERE id = ?"
        cursor.execute(query_select, (id,))
        fornecedorAntigo = cursor.fetchone()
        NomeFornecedorAntigo = fornecedorAntigo[1]

        query = "DELETE FROM Fornecedores WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()
        return {"message": f"Fornecedor {NomeFornecedorAntigo} foi deletado"}
    except Exception as e:
        return {"error": str(e)}
