
import sqlite3
from fastapi import APIRouter, HTTPException, status
from .modelos.modelos import *

router = APIRouter()

conn = sqlite3.connect('dados_farmacia.db')
cursor = conn.cursor()

# CRUD Funcionario
# ADD Funcionario
@router.post("/funcionarios/", status_code=status.HTTP_201_CREATED)
async def create_funcionario(funcionario: Funcionario):
    try:
        query = """INSERT INTO Funcionario 
                (p_nome, u_nome, cpf, unidade_trabalho, controle_farmacia) 
                VALUES (?, ?, ?, ?, ?)"""
        values = (
            funcionario.p_nome, funcionario.u_nome,
            funcionario.cpf, funcionario.unidade_trabalho, funcionario.controle_farmacia
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Funcionario {funcionario.p_nome} foi cadastrado com sucesso"}
    except Exception as e:
        return {"error": str(e)}

# LER Funcionario POR Matricula
@router.get("/funcionarios/{matricula}")
async def get_funcionario(matricula: int):
    try:
        query = "SELECT * FROM Funcionario WHERE matricula = ?"
        cursor.execute(query, (matricula,))
        dadosOne = cursor.fetchone()
        if not dadosOne:
            raise HTTPException(status_code=404, detail="Funcionario not found")
        funcionarioDados = {
            "matricula": dadosOne[0],
            "p_nome": dadosOne[1],
            "u_nome": dadosOne[2],
            "cpf": dadosOne[3],
            "unidade_trabalho": dadosOne[4],
            "controle_farmacia": dadosOne[5]
        }
        return {"funcionario": funcionarioDados}
    except Exception as e:
        return {"error": str(e)}

# PEGAR TODOS OS Funcionarios
@router.get("/funcionarios/")
async def getAll_funcionarios():
    try:
        query = "SELECT * FROM Funcionario"
        cursor.execute(query)
        dadosOne = cursor.fetchall()
        if not dadosOne:
            raise HTTPException(status_code=404, detail="Funcionario not found")
        funcionarioDados = []
        for dados in dadosOne:
            tempDados = {
                "matricula": dados[0],
                "p_nome": dados[1],
                "u_nome": dados[2],
                "cpf": dados[3],
                "unidade_trabalho": dados[4],
                "controle_farmacia": dados[5]
            }
            funcionarioDados.append(tempDados)

        return {"funcionarios": funcionarioDados}
    except Exception as e:
        return {"error": str(e)}

# ATUALIZAR Funcionario POR Matricula
@router.put("/funcionarios/{matricula}")
async def update_funcionario(matricula: int, funcionario: Funcionario):
    try:
        query = """UPDATE Funcionario SET 
                p_nome=?, u_nome=?, cpf=?, unidade_trabalho=?, controle_farmacia=?
                WHERE matricula=?"""
        values = (
            funcionario.p_nome, funcionario.u_nome, funcionario.cpf,
            funcionario.unidade_trabalho, funcionario.controle_farmacia, matricula
        )
        cursor.execute(query, values)
        conn.commit()
        return {"message": f"Funcionario {funcionario.p_nome} foi atualizado"}
    except Exception as e:
        return {"error": str(e)}

# DELETAR Funcionario POR Matricula
@router.delete("/funcionarios/{matricula}")
async def delete_funcionario(matricula: int):
    try:
        getNameQuery = "SELECT p_nome FROM Funcionario WHERE matricula = ?" 
        cursor.execute(getNameQuery, (matricula,)) 
        dadosOne = cursor.fetchone()
        
        if not dadosOne:
            return {"message": "Funcionario não encontrado"}        
        nomeCliente = dadosOne[0]

        query = "DELETE FROM Funcionario WHERE matricula = ?"
        cursor.execute(query, (matricula,))
        conn.commit()
        return {"message": f"Funcionario {nomeCliente} foi deleta do sistema"}
    except Exception as e:
        return {"error": str(e)}