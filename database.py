import sqlite3

class DataBase():
    def __init__(self, name = "System.db") -> None:
        self.name = name

    def conectar(self):
        self.connection = sqlite3.connect(self.name)

    def desconectar(self):
        try:
            self.connection.close()

        except:
            pass

    def criar_usuarios(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                CREATE TABLE IF NOT EXISTS users(

                    id           INTEGER  NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome         TEXT     NOT NULL,
                    usuario      TEXT     UNIQUE NOT NULL,
                    senha        TEXT     NOT NULL,                                                           
                    perfil       TEXT     NOT NULL

                );
            """)

        except AttributeError:
            print("faça a conexão com o banco de dados")

    def inserir_usuario(self, nome, usuario, senha, perfil):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                INSERT INTO users(nome, usuario, senha, perfil) VALUES(?,?,?,?)                        

            """,(nome, usuario, senha, perfil))

            self.connection.commit()

        except AttributeError:
            print("faça a conexão")  

        except sqlite3.IntegrityError:
            return 1
        

        def inserir_admin(self, nome, usuario, senha, perfil):
            try:
                cursor = self.connection.cursor()
                cursor.execute("""

                    INSERT INTO users(nome, usuario, senha, perfil) VALUES(admin,?,?,?)                        

                """,(nome, usuario, senha, perfil))

                self.connection.commit()

            except:
                return None    
                                  
    def checar_usuario(self, usuario, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users                       
            """)

            for linha in cursor.fetchall():
                if linha[2].upper() == usuario.upper() and linha[3] == senha:
                    return linha[4], linha[1]  

            return None

        except sqlite3.Error as e:
            print(f"Erro ao checar usuário no banco de dados: {e}")
            return None
                  
    def insert_data(self, full_dataset):
        cursor = self.connection.cursor()
        campos_tabela = ('NFe', 'serie', 'data_emissao', 'chave', 'cnpj_emitente', 'nome_emitente',
                        'valorNFe', 'itemNota', 'cod', 'qntd', 'descricao', 'unidade_medida', 'valorProd',
                        'data_importacao', 'usuario', 'data_saida')
        qntd = ','.join(map(str, '?' * 16))
        query = f"""INSERT INTO Notas ({', '.join(campos_tabela)}) VALUES ({qntd})"""

        try:
            for nota in full_dataset:
                cursor.execute(query, tuple(nota))
                self.connection.commit()

            return 1

        except sqlite3.IntegrityError:
            return 2

    def create_table_nfe(self):
        cursor = self.connection.cursor()
        cursor.execute (f"""

            CREATE TABLE IF NOT EXISTS Notas(
                        
            NFe             TEXT,
            serie           TEXT,
            data_emissao    TEXT,
            chave           TEXT,
            cnpj_emitente   TEXT,
            nome_emitente   TEXT,
            valorNFe        TEXT,
            itemNota        TEXT,
            cod             TEXT,
            qntd            TEXT,
            descricao       TEXT,
            unidade_medida  TEXT,
            valorProd       TEXT,
            data_importacao TEXT,
            usuario         TEXT,
            data_saida      TEXT,
                        
            PRIMARY KEY(chave, Nfe, itemNota)
                        
            );
        """)

    def uptdate_estoque(self, data_saida, usuario, notas):
        try:
            cursor = self.connection.cursor()
            for nota in notas:
                cursor.execute(f"""UPDATE Notas SET Data_saida = '{data_saida}', 
                usuario ='{usuario}' WHERE Nfe =  '{nota}'""")
                self.connection.commit()

        except AttributeError:
            print("faça a conexão para alterar campos")

    def update_estorno(self, notas):

        try:
            cursor = self.connection.cursor()

            for nota in notas:
                cursor.execute(f"UPDATE Notas SET Data_saida = '' WHERE NFe = {nota}"                               )

                self.connection.commit()

        except AttributeError:
            print('faça a conexão para alterar campos.')

    def update_usuario(self,nome,usuario,senha,perfil,id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""

                UPDATE users SET nome=?, usuario=? , senha=?, perfil=? WHERE id = ?
                    
                
            """,(nome, usuario, senha, perfil,id))

            self.connection.commit()    

        except AttributeError:
            print("erro ao atualizar usuario")

if __name__ == "__main__":
    db = DataBase()
    db.conectar()
    db.criar_usuarios()
    db.create_table_nfe()
    db.desconectar()             