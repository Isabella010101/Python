import sqlite3

# classe para gerenciar a conexão com o banco de dados sqlite
class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    # cria a tabela 'usuarios' se não existir
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            )
        ''')
        self.conn.commit()
    
    # insere um novo usuário no banco de dados
    def insert_user(self, nome):
        self.cursor.execute('INSERT INTO usuarios (nome) VALUES (?)', (nome,))
        self.conn.commit()

    # retorna todos os usuários do banco de dados
    def get_all_users(self):
        self.cursor.execute('SELECT * FROM usuarios')
        return self.cursor.fetchall()
    
    # atualiza o nome de um usuário existente
    def update_user(self, id, nome):
        self.cursor.execute('UPDATE usuarios SET nome=? WHERE id=?', (nome, id))
        self.conn.commit()

    # fecha a conexão com o banco de dados
    def close(self):
        self.conn.close()