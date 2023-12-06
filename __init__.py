import sqlite3

_farmacia = """
CREATE TABLE IF NOT EXISTS Farmacia (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    local TEXT
);"""

_medicamento = """CREATE TABLE IF NOT EXISTS Medicamento (
    id INTEGER PRIMARY KEY,
    vencimento DATE,
    preco DECIMAL(10,2),
    quantidade INTEGER,
    alergias TEXT,
    faixa_etaria TEXT,
    mg_ml TEXT,
    unidade TEXT,
    nome TEXT,
    farmacia_id INTEGER,
    similares INTEGER,
    genericos INTEGER,
    reabastecer INTEGER,
    compra_cliente INTEGER,
    FOREIGN KEY (farmacia_id) REFERENCES Farmacia(id)
);"""

_funcionario = """CREATE TABLE IF NOT EXISTS Funcionario (
    matricula INTEGER PRIMARY KEY,
    p_nome TEXT,
    u_nome TEXT,
    cpf TEXT,
    unidade_trabalho TEXT,
    controle_farmacia INTEGER,
    FOREIGN KEY (controle_farmacia) REFERENCES Farmacia(id)
);"""

_fornecedores = """CREATE TABLE IF NOT EXISTS Fornecedores (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    contato TEXT
);"""

_cliente = """CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cpf TEXT,
    telefone TEXT,
    email TEXT,
    alergias TEXT,
    cadastro_farmacia INTEGER,
    forma_pagamento TEXT,
    FOREIGN KEY (cadastro_farmacia) REFERENCES Farmacia(id)
);"""

conn = sqlite3.connect('dados_farmacia.db')
cursor = conn.cursor()
try:
    cursor.execute(_farmacia)
    cursor.execute(_medicamento)
    cursor.execute(_funcionario)
    cursor.execute(_fornecedores)
    cursor.execute(_cliente)
    conn.commit()
except Exception as e:
    print("error"+ str(e) )
