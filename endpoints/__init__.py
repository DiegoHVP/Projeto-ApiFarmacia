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
    compra_cliente INTEGER,
    FOREIGN KEY (farmacia_id) REFERENCES Farmacia(id),
    FOREIGN KEY (similares) REFERENCES Medicamento(id),
    FOREIGN KEY (genericos) REFERENCES Medicamento(id)
);"""

_funcionario = """CREATE TABLE IF NOT EXISTS Funcionario (
    matricula INTEGER PRIMARY KEY AUTOINCREMENT,
    p_nome TEXT,
    u_nome TEXT,
    cpf TEXT,
    unidade_trabalho TEXT,
    controle_farmacia INTEGER
);"""

_fornecedor = """CREATE TABLE IF NOT EXISTS Fornecedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    contato TEXT,
    medicamento_id INTEGER,
    FOREIGN KEY (medicamento_id) REFERENCES Medicamento(id)
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
    FOREIGN KEY (cadastro_farmacia) REFERENCES Farmacia(id)
);"""

_compra = """CREATE TABLE IF NOT EXISTS Compra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    medicamento_id INTEGER,
    data_compra DATE,
    quantidade INTEGER,
    preco_total DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    FOREIGN KEY (medicamento_id) REFERENCES Medicamento(id)
);"""

try:
    conn = sqlite3.connect("dados_farmacia.db")
    cursor = conn.cursor()
    cursor.execute(_farmacia)
    cursor.execute(_medicamento)
    cursor.execute(_funcionario)
    cursor.execute(_fornecedor)
    cursor.execute(_cliente)
    cursor.execute(_compra)
    conn.commit()
except sqlite3.Error as e:
    print("Erro ao executar query SQL:", e)
finally:
    conn.close()
