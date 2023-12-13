from typing import Optional
from pydantic import BaseModel

# MODELOS DE ENTIDADES
class Farmacia(BaseModel):
    nome: str
    local: Optional[str] = None

class Medicamento(BaseModel):
    vencimento: Optional[str] = None
    preco: float
    quantidade: Optional[int] = None
    alergias: Optional[str] = None
    faixa_etaria: Optional[str] = None
    mg_ml: Optional[str] = None
    unidade: Optional[str] = None
    nome: str
    farmacia_id: Optional[int] = None
    similares: Optional[int] = None
    genericos: Optional[int] = None
    reabastecer: Optional[int] = None

class Funcionario(BaseModel):
    p_nome: str
    u_nome: Optional[str] = None
    cpf: str
    unidade_trabalho: Optional[str] = None
    controle_farmacia: Optional[int] = None

class Fornecedor(BaseModel):
    nome: str
    contato: str
    medicamento_id: Optional[int] = None

class Cliente(BaseModel):
    nome: str
    cpf: str
    telefone: str
    email: Optional[str] = None
    alergias: Optional[str] = None
    cadastro_farmacia: Optional[int] = None
    forma_pagamento: Optional[str] = None

class Compra(BaseModel):
    cliente_id: Optional[int] = None
    medicamento_id: Optional[int] = None
    data_compra: Optional[str] = None
    quantidade: Optional[int] = None
    preco_total: Optional[float] = None
