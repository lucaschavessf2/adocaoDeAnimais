import os
import bcrypt
import sqlite3

class Conexao:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.criar_pastas()
        self.criar_tabelas()
        

    def criar_pastas(self):
        if os.path.exists("./database") == False:
            print('entrou')
            os.mkdir("./database")


    def iniciar(self):
        self.conn = sqlite3.connect("database/petmatch.db")
        self.cursor = self.conn.cursor()

    def encerrar(self):
        self.conn.commit()
        self.conn.close()

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
            cep TEXT,
            localizacao TEXT,
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
            temperamento TEXT,
            cor TEXT,
            raca TEXT,
            nome TEXT,
            descricao TEXT,
            recompensa TEXT,                                
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
        self.encerrar()

    def inserir_dados(self,tabela,colunas,dados):
        self.iniciar()
        interrogacao = "(?"
        for c in range(len(colunas.split(','))-1):
            interrogacao = interrogacao + ',?'
        interrogacao = interrogacao +')'
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
        
    def recomendar_pets(self,id_adotante):
        self.iniciar()
        self.cursor.execute("SELECT LOWER(especie), LOWER(estagio), LOWER(porte), LOWER(deficiencia), LOWER(criancas), LOWER(outros_animais), LOWER(temperamento) FROM adotantes WHERE id_usuario = ?", (id_adotante,))
        adotante = self.cursor.fetchone()
        print(adotante)
        if adotante:
            sql = f"""
            SELECT * FROM (SELECT 
                pets.*, 
                (
                    (CASE WHEN LOWER(pets.especie) = ? THEN 10 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.estagio) = ? THEN 3 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.porte) = ? THEN 2 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.deficiencia) = ? THEN 1 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.criancas) = ? THEN 1 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.outros_animais) = ? THEN 1 ELSE 0 END) +
                    (CASE WHEN LOWER(pets.temperamento) = ? THEN 1 ELSE 0 END)
                ) AS score
            FROM pets) as p  left join usuarios as us where p.id_usuario == us.id and p.id_usuario != {id_adotante}
            ORDER BY score DESC
            """

            self.cursor.execute(sql, adotante)
            recomendacoes = self.cursor.fetchall()
            self.encerrar()
            return recomendacoes
    def coletar_dados_usuario(self,id):
        print(id)
        if self.consultar_dados("adotantes", "COUNT(*)", "where id_usuario = ?", (id,))[0][0] > 0:
            dados = self.consultar_dados("usuarios","*",f"as u left join adotantes as a where u.id == a.id_usuario and u.id_login = ?",(id,))[0]
            dados_usuario = {
                "id":dados[1],
                "nome":dados[2],
                "data":dados[3],
                "cep":dados[4],
                "localizacao":dados[5],
                "telefone": dados[6],
                "especie" : dados[9],
                "estagio" : dados[10],
                "porte" : dados[11],
                "deficiencia" : dados[12],
                "criancas" : dados[13],
                "outros_animais" : dados[14],
                "temperamento" : dados[15],
            }
        else:
            dados = self.consultar_dados("usuarios","*","where id_login = ?",(id,))[0]
            dados_usuario = {
                "id":dados[1],
                "nome":dados[2],
                "data":dados[3],
                "cep":dados[4],
                "localizacao":dados[5],
                "telefone": dados[6],
                
            }
        print(dados_usuario)
        return dados_usuario



if __name__ == '__main__':
    c = Conexao()
    c.iniciar()
    c.cursor.execute('DROP TABLE adotados')
    c.encerrar()