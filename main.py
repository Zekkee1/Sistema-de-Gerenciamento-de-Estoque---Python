from PySide6.QtWidgets import(QApplication,QMainWindow,QMessageBox,QWidget, QFileDialog, QTreeWidgetItem)
from login import Ui_Login
from PySide6.QtCore import Qt
from tela_principal import Ui_MainWindow
from PySide6.QtGui import QIcon
import sys
from database import DataBase
from xml_files import Read_xml
import sqlite3
import pandas as pd
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import date
import matplotlib.pyplot as plt


class LoginWindow(QWidget,Ui_Login):
    def __init__(self):        
        super(LoginWindow, self).__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setWindowTitle("Login")
        self.ui.botton_login.clicked.connect(self.checar_login)

    def checar_login(self):
        self.users = DataBase()
        self.users.conectar()
        autenticado = self.users.checar_usuario(self.ui.txt_username.text().upper(), self.ui.txt_password.text())

        if autenticado:
            
            if autenticado[0] == "Administrador" or autenticado[0] == "Usuário":
                self.window = TelaPrincipal(autenticado)
                self.window.show()
                self.close()
                           
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Usuário não encontrado")
            msg.setWindowTitle("ERRO")
            msg.exec()

class TelaPrincipal(QMainWindow,Ui_MainWindow):
    def __init__(self,usuario):        
        super(TelaPrincipal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tela Principal") 
        self.usuario = usuario
        self.id_user = []
        
        
            
        self.ui.btn_excluir_usuarios.setVisible(self.usuario[0] =="Administrador")

        #---------------------------paginas------------------------#
        self.ui.Pages.setCurrentWidget(self.ui.page_home)
        self.ui.btn_home.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_home))
        self.ui.btn_outro.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_importar))
        self.ui.btn_tables.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_table))
        self.ui.btn_sobre.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_sobre))
        self.ui.btn_contato.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_contato))
        self.ui.btn_cadastro_usuario.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_cadastro))
        self.ui.btn_excluir_usuarios.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_usuarios))
        self.ui.btn_atualizar_usuario.clicked.connect(self.botao_atualizar)
        self.ui.btn_cancelar1.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_usuarios))
        self.ui.btn_cancelar2.clicked.connect(lambda:self.ui.Pages.setCurrentWidget(self.ui.page_usuarios))

        #------------------------cadastro-----------------------#
        self.ui.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.ui.btn_excluir_users.clicked.connect(self.excluir_usuarios)

        #-----------------------XML-----------------#
        self.ui.bnt_open_xml.clicked.connect(self.abrir_caminho)
        self.ui.btn_tables_2.clicked.connect(self.importar_xml)

        #---------------------filtro-----------------#
        self.ui.txt_filtro.textChanged.connect(self.filtro)
        self.ui.txt_filtro_usuario.textChanged.connect(self.filtro_usuario)

        #---------------saida e estorno -------------#
        self.ui.btn_saida.clicked.connect(self.gerar_saida)
        self.ui.btn_estornar.clicked.connect(self.gerar_estorno)
        self.ui.btn_excel.clicked.connect(self.excel_file)
        self.ui.btn_excluir.clicked.connect(self.excluir_itens_selecionados)
        self.ui.btn_grafico.clicked.connect(self.graphic)

        #---------------tb usuario---------------#
        self.ui.btn_confirmar.clicked.connect(self.atualizar_usuario)
        self.resetar_tabelas()

    def cadastrar_usuario(self):
        if self.ui.txt_senha.text() != self.ui.txt_confirmar_senha.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("SENHAS DIVERGENTES")
            msg.exec()          
            return None
        
        nome = self.ui.txt_nome.text()
        usuario = self.ui.txt_usuario.text()
        senha = self.ui.txt_senha.text()
        perfil = self.ui.box_perfil.currentText()
       
        db= DataBase()
        db.conectar()
        
        resposta = db.inserir_usuario(nome, usuario, senha, perfil)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)    
        if resposta == 1:
            msg.setText("usuario ja cadastrado")
        else:
            msg.setText("Cadastro Realizado Com Sucesso!!!")    
        msg.exec() 

        self.ui.txt_nome.setText("")
        self.ui.txt_usuario.setText("")
        self.ui.txt_senha.setText("")
        self.ui.txt_confirmar_senha.setText("")

        db.desconectar()
        self.resetar_tabelas()

    def abrir_caminho(self):
        self.path = QFileDialog.getExistingDirectory(self,str("Open Directory"),
                                                          "/home",
                                                          QFileDialog.ShowDirsOnly
                                       
                                                          | QFileDialog.DontResolveSymlinks)
        self.ui.lineEdit.setText(self.path)

    def importar_xml(self):
        msg = QMessageBox()
        msg.setWindowTitle("Importação XML")
        msg.setIcon(QMessageBox.Warning)

        if not self.ui.lineEdit.text():
            msg.setText("Selecione um diretório primeiro.")
            msg.exec()
            return
        
        xml = Read_xml(self.ui.lineEdit.text())
        all = xml.all_files()
                   
        db = DataBase()
        db.conectar()
        
        contador = 0
        contador2 = 0
        cont = 0

        for i in all:
            
            full_dataset = xml.nfe_data(i)
            cont += 1
            
            resposta2 = db.insert_data(full_dataset)
                        
            if resposta2 == 2:
                contador+=1

            elif resposta2 ==1:
                contador2 +=1
   

        if contador2 == 0:
            msg.setText("Nenhuma Nota foi cadastrada")
            msg.exec()
        else:
            msg.setText(f"{contador2} - Notas foram cadastrados com sucesso")
            msg.exec()
                                                             
        db.desconectar()

        self.resetar_tabelas()

    def tabela_estoque(self):       
        cn  =  sqlite3.connect('System.db')
        result = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida = ''", cn)
        result = result.values.tolist()
        column_to_hide = 14
        self.ui.tw_estoque.setColumnHidden(column_to_hide, True)
        
        self.x = ""

        for i in result:
            
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                
                self.campo = QTreeWidgetItem(self.ui.tw_estoque, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)

            self.x = i[0]

        self.ui.tw_estoque.setSortingEnabled(True)
   
        for i in range(1,15):
            self.ui.tw_estoque.resizeColumnToContents(i)
        
    def tabela_saida(self):
        cn  =  sqlite3.connect('System.db')
        result = pd.read_sql_query("""SELECT Nfe, serie, data_importacao, data_saida, usuario
         FROM Notas WHERE data_saida != ''""", cn)
        result = result.values.tolist()

        self.x = ""

        for i in result:
            
            if i[0] == self.x:
                QTreeWidgetItem(self.campo, i)
            else:
                self.campo = QTreeWidgetItem(self.ui.tw_saida, i)
                self.campo.setCheckState(0, Qt.CheckState.Unchecked)

            self.x = i[0]

        self.ui.tw_saida.setSortingEnabled(True)
   
        for i in range(1,15):
            self.ui.tw_saida.resizeColumnToContents(i)

    def tabela_geral(self):
        
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("System.db")
        db.open()

        self.model1 = QSqlTableModel(db=db)
        self.ui.tb_geral.setModel(self.model1)
        self.model1.setTable("Notas")
        self.model1.select()
                
    def resetar_tabelas(self):
        self.ui.tw_estoque.clear()
        self.ui.tw_saida.clear()

        self.tabela_saida()
        self.tabela_estoque()
        self.tabela_geral()
        self.tabela_usuarios()

    
        
    def filtro(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'Nfe LIKE "%{}%"'.format(s)
        self.model1.setFilter(filter_str)
      
    def gerar_saida(self):
        self.checked_items_out = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_items_out.append(child.text(0))
    
        recurse(self.ui.tw_estoque.invisibleRootItem())

        
        self.question('saída')

    def gerar_estorno(self):
        
        self.checked_items = []

        def recurse(parent_item):
            for i in range(parent_item.childCount()):
                child = parent_item.child(i)
                grand_children = child.childCount()
                if grand_children > 0:
                    recurse(child)
                if child.checkState(0) == Qt.Checked:
                    self.checked_items.append(child.text(0))

        recurse(self.ui.tw_saida.invisibleRootItem())
        self.question('estorno')
        
    def question(self, table):
        msgBox = QMessageBox()

        if table == 'estorno':
            msgBox.setText("Deseja estornar as notas selecionadas?")
            msgBox.setInformativeText("As selecionadas voltarão para o estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items}")

        else:
            msgBox.setText("Deseja Gerar saída das nota selecionadas?")
            msgBox.setInformativeText("As notas abaixo será baixada no estoque \n clique em 'Yes' para confirmar.")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msgBox.setDetailedText(f"Notas: {self.checked_items_out}")

        msgBox.setIcon(QMessageBox.Question)
        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            if table == "estorno":
                self.db = DataBase()
                self.db.conectar()
                self.db.update_estorno(self.checked_items)
                self.db.desconectar()
                self.resetar_tabelas()
            else:
                data_saida = date.today()
                data_saida = data_saida.strftime('%d/%m/%Y')
                self.db = DataBase()
                self.db.conectar()
                self.model.setTable("Users")
                self.db.uptdate_estoque(data_saida, self.usuario[1], self.checked_items_out)
                self.db.desconectar()
                self.resetar_tabelas()  

    def excel_file(self):

        cnx = sqlite3.connect('System.db')
        result = pd.read_sql_query("SELECT * FROM Notas", cnx)
        result.to_excel("Resumo de notas.xlsx", sheet_name='Notas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Relatório de Notas")
        msg.setText("Relatório gerado com sucesso!")
        msg.exec_()

    def graphic(self):
        cnx = sqlite3.connect("System.db")
        estoque = pd.read_sql_query('SELECT * FROM Notas', cnx)
        saida = pd.read_sql_query("SELECT * FROM Notas WHERE data_saida != ''", cnx)

        estoque = len(estoque)
        saida = len(saida)

        labels = "Estoque", "Saídas"
        sizes = [estoque, saida]
        axl = plt.subplots()
        axl.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        axl.axis("equal")

        plt.show()

    def tabela_usuarios(self):
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("System.db")
        db.open()

        self.model = QSqlTableModel(db=db)
        self.ui.tb_usuarios.setModel(self.model)
        self.model.setTable("users")
        senha_column_index = self.model.fieldIndex("senha")
        if senha_column_index != -1:
            self.model.removeColumn(senha_column_index)
        self.model.select()

    def excluir_itens_selecionados(self):
        selected_rows_geral = self.ui.tb_geral.selectionModel().selectedRows()
        msg = QMessageBox()

        if not selected_rows_geral:
            
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Exclusão de Itens")
            msg.setText("Nenhuma Nota foi selecionada")
            msg.exec()
            return  

        ids_to_delete1 = [str(self.model1.data(row.siblingAtColumn(0))) for row in selected_rows_geral]

        confirmation_msg = f"Deseja realmente excluir as seguintes notas fiscais?\n{', '.join(ids_to_delete1)}"

        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirmação de Exclusão")
        confirm_dialog.setText(confirmation_msg)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        ret = confirm_dialog.exec_()

        if ret == QMessageBox.Yes:
            db = DataBase()
            db.conectar()

            try:
                for id_to_delete1 in ids_to_delete1:
                    db.connection.execute(f"DELETE FROM Notas WHERE Nfe = '{id_to_delete1}'")
                    db.connection.commit()

                
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Exclusão de Itens")
                msg.setText("Itens excluídos com sucesso!")
                msg.exec_()

                self.resetar_tabelas()

            except sqlite3.Error as e:
                print(f"Erro ao excluir itens do banco de dados: {e}")

            finally:
                db.desconectar()
        else:
            return

    def excluir_usuarios(self):

        selected_rows = self.ui.tb_usuarios.selectionModel().selectedRows()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Usuário")

        if not selected_rows:
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Nenhum usuário selecionado para excluir.")
            msg.setText("Selecione um Usuário na tabela")
            msg.exec()
            return 
        
        ids_to_delete = [str(self.model.data(row.siblingAtColumn(0))) for row in selected_rows]
 
        confirmation_msg = f"Deseja realmente excluir o Usuário com o seguinte id: {', '.join(ids_to_delete)}"

        confirm_dialog = QMessageBox()
        confirm_dialog.setIcon(QMessageBox.Question)
        confirm_dialog.setWindowTitle("Confirmação de Exclusão")
        confirm_dialog.setText(confirmation_msg)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        ret = confirm_dialog.exec_()

        if ret == QMessageBox.Yes:
            db = DataBase()
            db.conectar()

            try:
                for id_to_delete in ids_to_delete:
                    if id_to_delete == "1": 
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText("Não é possivel excluir este usuario")
                        msg.exec()
                        
                        
                    else:    
                        db.connection.execute(f"DELETE FROM Users WHERE id = '{id_to_delete}'")
                        db.connection.commit()
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Exclusão de Itens")
                        msg.setText("Usuário excluido com sucesso!")
                        msg.exec_()
            
                self.resetar_tabelas()
                

            except sqlite3.Error as e:
                print(f"Erro ao excluir Usuário: {e}")

            finally:
                db.desconectar()
        else:
            return
        
    def atualizar_usuario(self):
        selected_rows = self.ui.tb_usuarios.selectionModel().selectedRows()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Usuário")
        
        
        if not selected_rows:       
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Nenhum usuário selecionado para atualizar.")
            msg.setText("Selecione um Usuário na tabela")
            
            msg.exec()
            return      
        self.id_user = str(self.model.data(selected_rows[0].siblingAtColumn(0)))

        nome = self.ui.txt_nome_atualizar.text()
        usuario = self.ui.txt_usuario_atualizar.text()
        senha = self.ui.txt_senha_atualizar.text()
        perfil = self.ui.box_perfil_atualizar.currentText()

        db = DataBase()
        db.conectar()

        db.update_usuario(nome, usuario, senha, perfil, self.id_user)
        msg.setText("Dados do usuário alterados com sucesso!")
        msg.exec()

        self.ui.txt_nome_atualizar.setText("")
        self.ui.txt_usuario_atualizar.setText("")
        self.ui.txt_senha_atualizar.setText("")
                            
        db.desconectar()


        self.resetar_tabelas()

    def filtro_usuario(self,s):
        s = re.sub("[\W_]+", "", s)
        filter_str = 'usuario LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)    
      
    def botao_atualizar(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Usuário")

        selected_rows = self.ui.tb_usuarios.selectionModel().selectedRows()


        if not selected_rows:    
            msg.setIcon(QMessageBox.Information)
            msg.setText("Nenhum usuário selecionado para atualizar.")
            msg.setText("Selecione um Usuário na tabela")
            msg.exec()
        else:
            self.ui.Pages.setCurrentWidget(self.ui.page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()        