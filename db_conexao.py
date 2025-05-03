import bcrypt
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
            email TEXT UNIQUE,
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

    

    def consultar_dados(self, tabela, colunas, filtro='', params=()):
        self.iniciar()
        sql = f"SELECT {colunas} FROM {tabela} {filtro}"
        print(sql)
        self.cursor.execute(sql, params)
        linhas = self.cursor.fetchall()
        self.encerrar()
        return linhas

    def verificar_login(self, email, senha):
        linhas = self.consultar_dados(
            "login_usuarios",
            "senha",
            "WHERE email = ?",
            (email,)
        )
        if not linhas:
            return False
        hash_senha_banco = linhas[0][0]
        if isinstance(hash_senha_banco, str):
            hash_senha_banco = hash_senha_banco.encode('utf-8')
        senha_bytes = senha.encode('utf-8')
        if bcrypt.checkpw(senha_bytes, hash_senha_banco):
            return True
        else:
            return False


        