from PyQt5 import  uic,QtWidgets
import sqlite3

from PyQt5.sip import delete


def listar_produtos():
    tela_2.show()
    banco = sqlite3.connect('banco_cadastro.db') 
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM dados")
    dados_lidos = cursor.fetchall()
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
           tela_2.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))
    
    banco.close()
    

def salvar_dados():
    id = tela.lineEdit_5.text()
    produto = tela.lineEdit.text()
    quantidade = tela.lineEdit_3.text()
    valor = tela.lineEdit_2.text()
    validade = tela.lineEdit_4.text()
    
    try:
        banco = sqlite3.connect('banco_cadastro.db') 
        cursor = banco.cursor()
        cursor.execute("INSERT INTO dados VALUES ('"+id+"','"+produto+"','"+quantidade+"','"+valor+"','"+validade+"')")
        
        banco.commit() 
        banco.close()
        tela.lineEdit_5.setText("")
        tela.lineEdit.setText("")
        tela.lineEdit_2.setText("")
        tela.lineEdit_3.setText("")
        tela.lineEdit_4.setText("")
        print("Dados inseridos com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados: ",erro)
        
              

def delete(id):
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    id = tela_2.lineEdit.text()
    id = int(id)
    cursor.execute ("DELETE FROM dados WHERE id="+ str(id))
    banco.commit() 
                
    print(cursor.fetchall())

    banco.close()
    tela_2.close()

       
app=QtWidgets.QApplication([])
tela=uic.loadUi("cadastro.ui")
tela_2 = uic.loadUi("estoque.ui")
tela.pushButton.clicked.connect(salvar_dados)
tela.pushButton_2.clicked.connect(listar_produtos)
tela_2.pushButton_3.clicked.connect(delete)


tela.show()
app.exec()


