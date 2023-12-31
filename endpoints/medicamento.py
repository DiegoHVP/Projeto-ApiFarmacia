
import sqlite3
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *

router = APIRouter()

conn = sqlite3.connect('dados_farmacia.db')
cursor = conn.cursor()


# CRUD para Medicamento
# ADD Medicamento
@router.post("/medicamento/", status_code=status.HTTP_201_CREATED)
async def create_medicamento(m: Medicamento):
    try:
        query = """INSERT INTO Medicamento 
                (vencimento, preco, quantidade, alergias, faixa_etaria, mg_ml, unidade, nome, farmacia_id, similares, genericos, reabastecer) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = ( 
            m.vencimento, m.preco, m.quantidade,
            m.alergias, m.faixa_etaria, m.mg_ml,
            m.unidade, m.nome, m.farmacia_id,
            m.similares, m.genericos,
            m.reabastecer
        )
        
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Medicamento criado com sucesso"}
    except Exception as e:
        return {"error": str(e)}

# GET Medicamento por ID
@router.get("/medicamento/{id}")
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
            "alergias": dadosOne[4],
            "faixa_etaria": dadosOne[5],
            "mg_ml": dadosOne[6],
            "unidade": dadosOne[7],
            "farmacia_id": dadosOne[9],
            "similares": dadosOne[10],
            "genericos": dadosOne[11],
            "reabastecer": dadosOne[12]
        }
        return {"Medicamento": medicamentoDados}
    except Exception as e:
        return {"error": str(e)}

# GET Todos os Medicamentos
@router.get("/medicamento/")
async def get_all_medicamento():
    try:
        query = "SELECT * FROM Medicamento"
        cursor.execute(query)
        dadosAll = cursor.fetchall()
        
        medicamentosDados = []
        for dadosOne in dadosAll:
            tempDados =  {
                "id": dadosOne[0],
                "nome": dadosOne[8],
                "preco": dadosOne[2],
                "mg_ml": dadosOne[6],
                "vencimento": dadosOne[1],
                "quantidade": dadosOne[3],
                "alergias": dadosOne[4],
                "faixa_etaria": dadosOne[5],
                "unidade": dadosOne[7],
                "farmacia_id": dadosOne[9],
                "similares": dadosOne[10],
                "genericos": dadosOne[11],
                "reabastecer": dadosOne[12]
            }
            medicamentosDados.append(tempDados)

        if len(medicamentosDados)!=0:
            return {"Medicamentos" : medicamentosDados}
        else:
            return {"message":"Não há medicamentos cadastrados"}
        
    except Exception as e:
        return {"error": str(e)}

# UPDATE Medicamento por ID
@router.put("/medicamento/{id}")
async def update_medicamento(id: int, medicamento: Medicamento):
    try:
        verificar = "SELECT id FROM Medicamento WHERE id = ?"
        cursor.execute(verificar, (id,))
        medicamentoBool = cursor.fetchone()

        if not medicamentoBool:
            return {"error": f"Medicamento com ID {id} não encontrado"}

        query = """UPDATE Medicamento SET 
                vencimento=?, preco=?, quantidade=?, alergias=?, faixa_etaria=?, 
                mg_ml=?, unidade=?, nome=?, farmacia_id=?, similares=?, genericos=?, reabastecer=?
                WHERE id=?"""
        values = (
            medicamento.vencimento, medicamento.preco, medicamento.quantidade,
            medicamento.alergias, medicamento.faixa_etaria, medicamento.mg_ml,
            medicamento.unidade, medicamento.nome, medicamento.farmacia_id,
            medicamento.similares, medicamento.genericos,
            medicamento.reabastecer, id
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Medicamento {medicamento.nome} foi atualizado"}
    except Exception as e:
        return {"error": str(e)}

# DELETE Medicamento por ID
@router.delete("/medicamento/{id}")
async def delete_medicamento(id: int):
    try:
        query_select = "SELECT * FROM Medicamento WHERE id = ?"
        cursor.execute(query_select, (id,))
        dadosOne = cursor.fetchone()

        if not dadosOne:
            return {"message": "Medicamento não encontrado"}

        nomeMedicamento = dadosOne[8]  # Pega o nome do Medicamento

        query_delete = "DELETE FROM Medicamento WHERE id = ?"
        cursor.execute(query_delete, (id,))
        conn.commit()

        return {"message": f"Medicamento {nomeMedicamento} foi deletado"}
    except Exception as e:
        return {"error": str(e)}
