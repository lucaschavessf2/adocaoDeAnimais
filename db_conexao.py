import os
import bcrypt
import sqlite3

#Classe responsável por fazer a conexão com o banco
class Conexao:
    #Inicia as variáveis globais da classe  e starta algumas funções
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.criar_pastas()
        self.criar_tabelas()
        

    def criar_pastas(self):
        if os.path.exists("./database") == False:
            print('entrou')
            os.mkdir("./database")


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
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS login_usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            senha TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_login INTEGER,
            nome TEXT,
            data_nascimento DATE,
            endereco TEXT,
            telefone TEXT,
            FOREIGN KEY (id_login) REFERENCES login_usuarios(id)
        )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            especie TEXT,
            estagio TEXT,
            porte TEXT,
            deficiencia TEXT,
            criancas TEXT,
            outros_animais TEXT,
            temperamento TEXT,
            cor TEXT,
            raca TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS perdidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            especie TEXT,
            estagio TEXT,
            porte TEXT,
            deficiencia TEXT,
            criancas TEXT,
            outros_animais TEXT,
            temperamento TEXT,
            cor TEXT,
            raca TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS adotantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            especie TEXT,
            estagio TEXT,
            porte TEXT,
            deficiencia TEXT,
            criancas TEXT,
            outros_animais TEXT,
            temperamento TEXT,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS adotados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER,
            especie TEXT,
            estagio DATE,
            cor TEXT,
            raca INTEGER,
            FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
        )
        """)
        self.encerrar()

    #Função que insere os dados em uma tabela
    def inserir_dados(self,tabela,colunas,dados):
        self.iniciar()
        interrogacao = "(?"
        for c in range(len(colunas.split(','))-1):
            interrogacao = interrogacao + ',?'
        interrogacao = interrogacao +')'
        print('---------------',interrogacao)
        sql = f"""INSERT INTO {tabela} {colunas} VALUES {interrogacao}"""
        print(sql)
        self.cursor.execute(sql,dados)
        ultimo_id = self.cursor.lastrowid
        self.encerrar()
        print(self.consultar_dados(tabela,"*"))
        return ultimo_id
    
    def deletar_dados(self, tabela, filtro='', params=()):
        self.iniciar()
        sql = f"DELETE FROM {tabela} {filtro}"
        print(sql)
        self.cursor.execute(sql, params)
        self.encerrar()

    def atualizar_dados(self,tabela,colunas,dados,filtro=''):
        self.iniciar()
        set_colunas = ""
        for i,coluna in enumerate(colunas.split(',')):
            set_colunas = set_colunas+coluna.replace('(','').replace(')','')+" = ?,"
        set_colunas = set_colunas[:-1]
        sql = f"""UPDATE {tabela} SET {set_colunas} {filtro}"""
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
            "senha,id",
            "WHERE email = ?",
            (email,)
        )
        if not linhas:
            return [False]
        print(linhas)
        hash_senha_banco = linhas[0][0]
        id_usuario = linhas[0][1]
        if isinstance(hash_senha_banco, str):
            hash_senha_banco = hash_senha_banco.encode('utf-8')
        senha_bytes = senha.encode('utf-8')
        if bcrypt.checkpw(senha_bytes, hash_senha_banco):
            return [True,id_usuario]
        else:
            return [False]
        
    def coletar_dados_usuario(self,id):
        print(id)
        # dados = self.consultar_dados("usuarios","*",f"as u left join adotantes as a where u.id == a.id_usuario and u.id_login == ?",(id,))
        if self.consultar_dados("adotantes", "COUNT(*)", "where id_usuario = ?", (id,))[0][0] > 0:
            dados = self.consultar_dados("usuarios","*",f"as u left join adotantes as a where u.id == a.id_usuario and u.id_login = ?",(id,))[0]
            dados_usuario = {
                "id":dados[1],
                "nome":dados[2],
                "data":dados[3],
                "endereco":dados[4],
                "telefone": dados[5],
                "especie" : dados[8],
                "estagio" : dados[9],
                "porte" : dados[10],
                "deficiencia" : dados[11],
                "criancas" : dados[12],
                "outros_animais" : dados[13],
                "temperamento" : dados[14],
            }
        else:
            dados = self.consultar_dados("usuarios","*","where id_login = ?",(id,))[0]
            dados_usuario = {
                "id":dados[1],
                "nome":dados[2],
                "data":dados[3],
                "endereco":dados[4],
                "telefone": dados[5],
            }
        print(dados_usuario)
        return dados_usuario


if __name__ == '__main__':
    print('x')
    c = Conexao()
    print(c.consultar_dados("usuarios","*",f"as u left join adotantes as a where u.id == a.id_usuario and u.id_login = ?",(1,)))