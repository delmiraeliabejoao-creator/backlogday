import sqlite3

def conectar():
    return sqlite3.connect("backlogday.db")

def executar(comando, parametros=()):
    bd = conectar()
    cursor = bd.cursor()
    cursor.execute(comando, parametros)
    bd.commit()
    bd.close()

def consultar(comando, parametros=()):
    bd = conectar()
    cursor = bd.cursor()
    cursor.execute(comando, parametros)
    resultado = cursor.fetchall()
    bd.close()
    return resultado

def iniciar_banco():
    executar('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        senha TEXT,
        perfil TEXT
    )''')

        executar('''CREATE TABLE IF NOT EXISTS ordens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        tipo_equipamento TEXT,
        codigo_equipamento TEXT,
        itens_pendentes TEXT,
        descricao TEXT,
        status TEXT DEFAULT 'Aguardando Serviço',
        mecanico TEXT,
        solicitante TEXT,
        midia TEXT
    )''')

    executar('''CREATE TABLE IF NOT EXISTS pedidos_pecas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ordem INTEGER,
        quantidade INTEGER,
        codigo_peca TEXT,
        nome_peca TEXT,
        solicitante TEXT,
        tipo_equipamento TEXT
    )''')

    try:
        executar("INSERT INTO usuarios (email, senha, perfil) VALUES (?, ?, ?)",
                 ("admin@backlogday.com", "admin123", "Administrador"))
    except:
        pass
