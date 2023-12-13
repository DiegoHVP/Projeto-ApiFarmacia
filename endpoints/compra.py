import sqlite3, datetime
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *


router = APIRouter()

conn = sqlite3.connect("dados_farmacia.db")
cursor = conn.cursor()

# CRUD Compra
# ADD Compra
@router.post("/compra/", status_code=status.HTTP_201_CREATED)
async def create_compra(compra: Compra):
    try:
        cursor.execute("SELECT * FROM Medicamento WHERE id = ?", (compra.medicamento_id,))
        medicamentoExiste = cursor.fetchone()
        if not medicamentoExiste:
            raise HTTPException(status_code=404, detail="Medicamento informado não encontrado")
        
        cursor.execute("SELECT * FROM Cliente WHERE id = ?", (compra.cliente_id,))
        clienteExiste = cursor.fetchone()
        if not clienteExiste:
            raise HTTPException(status_code=404, detail="Cliente informado não encontrado")
        
        dataSql = datetime.datetime.now().strftime('%Y-%m-%d')
        query = "INSERT INTO Compra (cliente_id, medicamento_id, data_compra, quantidade, preco_total) VALUES (?, ?, ?, ?, ?)"
        values = (
            compra.cliente_id,
            compra.medicamento_id,
            dataSql,
            compra.quantidade,
            compra.preco_total
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Compra registrada com sucesso"}
    except Exception as e:
        return {"error": str(e)}



# GET Compra POR ID
@router.get("/compra/{id}")
async def get_compra(id: int):
    try:
        query = "SELECT * FROM Compra WHERE id = ?"
        cursor.execute(query, (id,))
        dadosOne = cursor.fetchone()
        if not dadosOne:
            raise HTTPException(status_code=404, detail="Compra não encontrada")
        
        compra_info = {
            "id": dadosOne[0],
            "cliente_id": dadosOne[1],
            "medicamento_id": dadosOne[2],
            "data_compra": dadosOne[3],
            "quantidade": dadosOne[4],
            "preco_total": dadosOne[5]
        }
        
        return {"Compra": compra_info}
    except Exception as e:
        return {"error": str(e)}

# GET TODAS AS Compras
@router.get("/compra/")
async def get_all_compras():
    try:
        query = "SELECT * FROM Compra"
        cursor.execute(query)
        dadosAll = cursor.fetchall()
        if not dadosAll:
            raise HTTPException(status_code=404, detail="Nenhuma compra encontrada")
        
        compras_info = []
        for dadosOne in dadosAll:
            compra_info = {
                "id": dadosOne[0],
                "cliente_id": dadosOne[1],
                "medicamento_id": dadosOne[2],
                "data_compra": dadosOne[3],
                "quantidade": dadosOne[4],
                "preco_total": dadosOne[5]
            }
            compras_info.append(compra_info)
        
        return {"Compras": compras_info}
    except Exception as e:
        return {"error": str(e)}

# ATUALIZAR Compra POR ID
@router.put("/compra/{id}")
async def update_compra(id: int, compra: Compra):
    try:
        check_query = "SELECT id FROM Compra WHERE id = ?"
        cursor.execute(check_query, (id,))
        compraBool = cursor.fetchone()
        if not compraBool:
            return {"error": f"Compra com ID {id} não encontrada"}

        cursor.execute("SELECT * FROM Medicamento WHERE id = ?", (compra.medicamento_id,))
        medicamentoExiste = cursor.fetchone()
        if not medicamentoExiste:
            raise HTTPException(status_code=404, detail="Medicamento informado não encontrado")
        
        cursor.execute("SELECT * FROM Cliente WHERE id = ?", (compra.cliente_id,))
        clienteExiste = cursor.fetchone()
        if not clienteExiste:
            raise HTTPException(status_code=404, detail="Cliente informado não encontrado")

        query = "UPDATE Compra SET medicamento_id=?, quantidade=?, preco_total=? WHERE id=?"
        values = (
            compra.medicamento_id,
            compra.quantidade,
            compra.preco_total,
            id
        )
        cursor.execute(query, values)
        conn.commit()
        
        return {"message": f"Compra com ID {id} foi atualizada"}
    except Exception as e:
        return {"error": str(e)}

# DELETAR Compra POR ID
@router.delete("/compra/{id}")
async def delete_compra(id: int):
    try:
        select_query = "SELECT * FROM Compra WHERE id = ?"
        cursor.execute(select_query, (id,))
        compra_data = cursor.fetchone()
        if not compra_data:
            return {"error": f"Compra com ID {id} não encontrada"}

        query = "DELETE FROM Compra WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()
        return {"message": f"Compra com ID {id} foi deletada"}
    except Exception as e:
        return {"error": str(e)}
