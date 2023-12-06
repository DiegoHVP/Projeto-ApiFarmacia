from typing import Optional  
from pydantic import BaseModel

# MODELOS DE ENTIDADES
class Medicamento(BaseModel):
    vencimento: Optional[str] = None
    preco: float
    quantidade: Optional[str] = None
    alergias: Optional[str] = None
    faixa_etaria: Optional[str] = None
    mg_ml: Optional[str] = None
    unidade: Optional[str] = None
    nome: str
    farmacia_id: Optional[str] = None

class Funcionario(BaseModel):
    p_nome: str
    u_nome: Optional[str] = None
    cpf: str
    unidade_trabalho: Optional[str] = None
    controle_farmacia: Optional[int] = None

class Fornecedor(BaseModel):
    nome: str
    contato: str

class Cliente(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: Optional[str] = None
    alergias: Optional[str] = None
    cadastro_farmacia: Optional[int] = None
    forma_pagamento: Optional[str] = None
    
class Farmacia(BaseModel):
  nome: str
  local: Optional[str] = None