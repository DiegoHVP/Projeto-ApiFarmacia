
import sqlite3
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *

router = APIRouter()

conn = sqlite3.connect('dados_farmacia.db')
cursor = conn.cursor()


# CRUD Cliente
# CRIAR Cliente
@router.post("/clientes/", status_code=status.HTTP_201_CREATED)
async def create_cliente(c: Cliente):
    try:
        query = """INSERT INTO Cliente
                (nome, cpf, telefone, email, alergias, cadastro_farmacia, forma_pagamento) 
                VALUES (?, ?, ?, ?, ?, ?, ?)"""
        values = (
            c.nome, c.cpf, c.telefone,
            c.email, c.alergias, c.cadastro_farmacia,
            c.forma_pagamento
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Cliente {c.nome} foi cadastrado com sucesso"}
    except Exception as e:
        return {"error": str(e)}


# LER Cliente POR ID
@router.get("/clientes/{cliente_id}")
async def get_cliente(cliente_id: int):
    try:
        query = "SELECT * FROM Cliente WHERE id = ?"
        cursor.execute(query, (cliente_id,))
        cliente = cursor.fetchone()
        if not cliente:
            raise HTTPException(status_code=404, detail="Cliente not found")
        cliente_Dados = {
            "id": cliente[0],
            "nome": cliente[1],
            "cpf": cliente[2],
            "telefone": cliente[3],
            "email": cliente[4],
            "alergias": cliente[5],
            "cadastro_farmacia": cliente[6],
            "forma_pagamento": cliente[7]
        }
        return {"Cliente": cliente_Dados}
    except Exception as e:
        return {"error": str(e)}

# PEGAR TODOS OS Clientes
@router.get("/clientes/")
async def getAll_clientes():
    try:
        query = """SELECT * FROM Cliente"""
        cursor.execute(query)
        
        dadosAll = cursor.fetchall()
        clientesDados = []
        for dadosOne in dadosAll:
            tempDados = {
                "id": dadosOne[0],
                "nome": dadosOne[1],
                "cpf": dadosOne[2],
                "telefone": dadosOne[3],
                "email": dadosOne[4],
                "alergias": dadosOne[5],
                "cadastro_farmacia": dadosOne[6],
                "forma_pagamento": dadosOne[7]
            }
            clientesDados.append(tempDados)
        return {"Clientes" : clientesDados}
    except Exception as e:
        return {"error": str(e)}


# ATUALIZAR Cliente POR ID
@router.put("/clientes/{id}")
async def update_cliente(id: int, c: Cliente):
    try:
        query = """UPDATE Cliente AS C SET 
                nome=?, cpf=?, telefone=?, email=?, alergias=?, 
                cadastro_farmacia=?, forma_pagamento=?
                WHERE id=?"""
        values = (
            c.nome, c.cpf, c.telefone, c.email,
            c.alergias, c.cadastro_farmacia, c.forma_pagamento,
            id
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Cliente {c.nome} foi atualizado"}
    except Exception as e:
        return {"error": str(e)}


# DELETAR Cliente POR ID
@router.delete("/clientes/{cliente_id}")
async def delete_cliente(cliente_id: int):
    try:
        query_get_name = "SELECT nome FROM Cliente WHERE id = ?" 
        cursor.execute(query_get_name, (cliente_id,)) 
        dados = cursor.fetchone()
        
        if not dados:
            return {"message": "Cliente não encontrado"}
        
        nome_cliente = dados[0]  #PEGA O NOME DO CLIENTE

        query_delete = "DELETE FROM Cliente WHERE id = ?"
        cursor.execute(query_delete, (cliente_id,))
        conn.commit()
        
        return {"message": f"Cliente {nome_cliente} foi deletado do sistema"}
    except Exception as e:
        return {"error": str(e)}
