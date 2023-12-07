
import sqlite3
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *

router = APIRouter()

conn = sqlite3.connect('dados_farmacia.db')
cursor = conn.cursor()


# CRUD para Medicamento
# ADD Medicamento
@router.post("/medicamentos/", status_code=status.HTTP_201_CREATED)
async def create_medicamento(m: Medicamento):
    try:
        query = """INSERT INTO Medicamento 
                (vencimento, preco, quantidade, alergias, faixa_etaria, mg_ml, unidade, nome, farmacia_id) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = ( 
            m.vencimento, m.preco, m.quantidade,
            m.alergias, m.faixa_etaria, m.mg_ml,
            m.unidade, m.nome, m.farmacia_id
        )
        
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Medicamento criado com sucesso"}
    except Exception as e:
        return {"error": str(e)}

# LER Medicamento POR ID
@router.get("/medicamentos/{id}")
async def get_medicamento(id: int):
    try:
        query = "SELECT * FROM Medicamento WHERE id = ?"
        cursor.execute(query, (id,))
        dadosOne = cursor.fetchone()

        if not dadosOne:
            raise HTTPException(status_code=404, detail="Medicamento não encontrado")
        
        medicamentoDados = {
            "id": dadosOne[0],
            "nome": dadosOne[8],
            "vencimento": dadosOne[1],
            "preco": dadosOne[2],
            "quantidade": dadosOne[3],
            "alergias": dadosOne[5],
            "faixa_etaria": dadosOne[5],
            "mg_ml": dadosOne[6],
            "unidade": dadosOne[7],
            "farmacia_id": dadosOne[9]
        }
        return {"Medicamento": medicamentoDados}
    except Exception as e:
        return {"error": str(e)}

# LER TODOS OS Medicamento
@router.get("/medicamentos/")
async def get_medicamento():
    try:
        query = "SELECT * FROM Medicamento"
        cursor.execute(query)
        dadosAll = cursor.fetchall()
        
        if not dadosAll:
            raise HTTPException(status_code=404, detail="Medicamentos não encontrado")
        
        medicamentosDados = []
        for dadosOne in dadosAll:
            tempDados =  {
                "id": dadosOne[0],
                "nome": dadosOne[8],
                "vencimento": dadosOne[1],
                "preco": dadosOne[2],
                "quantidade": dadosOne[3],
                "alergias": dadosOne[5],
                "faixa_etaria": dadosOne[5],
                "mg_ml": dadosOne[6],
                "unidade": dadosOne[7],
                "farmacia_id": dadosOne[9]
            }
            medicamentosDados.append(tempDados)
        return {"Medicamento": medicamentosDados}
    except Exception as e:
        return {"error": str(e)}

# ATUALIZAR Medicamento POR ID
@router.put("/medicamentos/{id}")
async def update_medicamento(id: int, m: Medicamento):
    try:
        query = """UPDATE Medicamento SET 
                vencimento=?, preco=?, quantidade=?, alergias=?, faixa_etaria=?, 
                mg_ml=?, unidade=?, nome=?, farmacia_id=?
                WHERE id=?"""
        values = (
            m.vencimento, m.preco, m.quantidade,
            m.alergias, m.faixa_etaria, m.mg_ml,
            m.unidade, m.nome, m.farmacia_id, id
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Medicamento {m.nome} foi atualizado"}
    except Exception as e:
        return {"error": str(e)}


# DELETAR Medicamento POR ID
@router.delete("/medicamentos/{id}")
async def delete_medicamento(id: int):
    try:
        query_select = "SELECT * FROM Medicamento WHERE id = ?"
        cursor.execute(query_select, (id,))
        dadosOne = cursor.fetchone()

        if not dadosOne:
            return {"message": "Medicamento não encontrado"}

        nomeMedicamento = dadosOne[8] #PEGA NOME

        query_delete = "DELETE FROM Medicamento WHERE id = ?"
        cursor.execute(query_delete, (id,))
        conn.commit()

        return {"message": f"Medicamento {nomeMedicamento} foi deletado"}
    except Exception as e:
        return {"error": str(e)}
