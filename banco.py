import sqlite3

def iniciar_banco():
    conn = sqlite3.connect("backlogday.db")
    cursor = conn.cursor()

    # Tabela de Usuários
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        senha TEXT,
        perfil TEXT
    )''')

    # Tabela de Ordens
    def iniciar_banco():
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

    # Tabela de Pedidos de Peças
    cursor.execute('''CREATE TABLE IF NOT EXISTS pedidos_pecas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ordem INTEGER,
        quantidade INTEGER,
        codigo_peca TEXT,
        nome_peca TEXT,
        solicitante TEXT,
        tipo_equipamento TEXT,
        FOREIGN KEY (id_ordem) REFERENCES ordens(id)
    )''')

    # Cria usuário ADMIN padrão se não existir
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", ("admin@backlogday.com",))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO usuarios (email, senha, perfil) VALUES (?, ?, ?)",
                      ("admin@backlogday.com", "admin123", "Administrador"))

    conn.commit()
    conn.close()

def executar(sql, params=()):
    conn = sqlite3.connect("backlogday.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    conn.close()

def consultar(sql, params=()):
    conn = sqlite3.connect("backlogday.db")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    res = cursor.fetchall()
    conn.close()
    return res
