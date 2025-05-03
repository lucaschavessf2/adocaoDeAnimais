import sqlite3

class Conexao:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.criar_tabelas()

    def iniciar(self):
        self.conn = sqlite3.connect("database/adopet.db")
        self.cursor = self.conn.cursor()

    def encerrar(self):
        self.conn.commit()
        self.conn.close()

    def criar_tabelas(self):
        self.iniciar()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS login_usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            senha TEXT
            );
        """)
        self.encerrar()

    def inserir_dados(self,tabela,colunas,dados):
        self.iniciar()
        sql = f"""INSERT INTO {tabela} {colunas} VALUES (?, ?)"""
        print(sql)
        self.cursor.execute(sql,dados)
        self.encerrar()
        print(self.consultar_dados(tabela,"*"))

    def consultar_dados(self,tabela,colunas,filtro=''):
        self.iniciar()
        sql = f"""SELECT {colunas} FROM {tabela} """+filtro
        print(sql)
        self.cursor.execute(sql)
        linhas = self.cursor.fetchall()
        self.encerrar()
        return linhas

    def verificar_login(self,email,senha):
        linhas = self.consultar_dados("login_usuarios","COUNT(*)",f"WHERE email = '{email}' and senha = '{senha}'")
        if linhas[0][0] > 0:
            return True
        else:
            return False
        