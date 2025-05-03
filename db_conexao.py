import bcrypt
import sqlite3

#Classe responsável por fazer a conexão com o banco
class Conexao:
    #Inicia as variáveis globais da classe  e starta algumas funções
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.criar_tabelas()

    #Função responsável por se conectar ao banco
    def iniciar(self):
        self.conn = sqlite3.connect("database/adopet.db")
        self.cursor = self.conn.cursor()

    #Função que finaliza o comando no banco e encerra a conexão
    def encerrar(self):
        self.conn.commit()
        self.conn.close()

    #Função que cria as tabelas necessárias
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

    #Função que insere os dados em uma tabela
    def inserir_dados(self,tabela,colunas,dados):
        self.iniciar()
        sql = f"""INSERT INTO {tabela} {colunas} VALUES (?, ?)"""
        print(sql)
        self.cursor.execute(sql,dados)
        self.encerrar()
        print(self.consultar_dados(tabela,"*"))

    
    #Função que consulta os dados em uma tabela e retorna suas linhas
    def consultar_dados(self, tabela, colunas, filtro='', params=()):
        self.iniciar()
        sql = f"SELECT {colunas} FROM {tabela} {filtro}"
        print(sql)
        self.cursor.execute(sql, params)
        linhas = self.cursor.fetchall()
        self.encerrar()
        return linhas

    #Função para verificar se o login existe
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


        