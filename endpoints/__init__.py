import sqlite3

_farmacia = """ CREATE TABLE IF NOT EXISTS Farmacia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    local TEXT
); """

_medicamento = """CREATE TABLE IF NOT EXISTS Medicamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
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
    FOREIGN KEY (farmacia_id) REFERENCES Farmacia(id) ON DELETE CASCADE,
    FOREIGN KEY (similares) REFERENCES Medicamento(id) ON DELETE CASCADE,
    FOREIGN KEY (genericos) REFERENCES Medicamento(id) ON DELETE CASCADE
);"""

_farmaceutico = """CREATE TABLE IF NOT EXISTS Farmaceutico (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    p_nome TEXT,
    u_nome TEXT,
    cpf TEXT,
    unidade_trabalho TEXT,
    controle_farmacia INTEGER,
    senha TEXT
);"""

_fornecedor = """CREATE TABLE IF NOT EXISTS Fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    contato TEXT,
    medicamento_id INTEGER,
    FOREIGN KEY (medicamento_id) REFERENCES Medicamento(id) ON DELETE CASCADE
);"""

_cliente = """CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cpf TEXT,
    telefone TEXT,
    email TEXT,
    alergias TEXT,
    cadastro_farmacia INTEGER,
    forma_pagamento TEXT,
    senha TEXT,
    sobrenome TEXT,
    FOREIGN KEY (cadastro_farmacia) REFERENCES Farmacia(id) ON DELETE CASCADE
);"""

_compra = """CREATE TABLE IF NOT EXISTS Compra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    data_compra DATE,
    quantidade INTEGER,
    preco_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id) ON DELETE CASCADE
);"""

_compra_medicamento = """CREATE TABLE IF NOT EXISTS Compra_Medicamento (
    compra_id INTEGER,
    medicamento_id INTEGER,
    quantidade INTEGER,
    PRIMARY KEY (compra_id, medicamento_id),
    FOREIGN KEY (compra_id) REFERENCES Compra(id) ON DELETE CASCADE,
    FOREIGN KEY (medicamento_id) REFERENCES Medicamento(id) ON DELETE CASCADE
);"""


try:
    conn = sqlite3.connect("dados_farmacia.db")
    cursor = conn.cursor()
    cursor.execute(_farmacia)
    cursor.execute(_medicamento)
    cursor.execute(_farmaceutico)
    cursor.execute(_fornecedor)
    cursor.execute(_cliente)
    cursor.execute(_compra)
    cursor.execute(_compra_medicamento)
    conn.commit()
except sqlite3.Error as e:
    print("Erro ao executar query SQL:", e)
finally:
    conn.close()
