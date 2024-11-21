# importar o drive de comunicação do Python com o MySQL
import mysql.connector as myc

# vamos criar uma função para estabelecer a conexão com o banco de dados
# todas as vezes que for executar uma consulta em uma das tabelas, esta
# função pode ser utilizada.
def conectar_banco():
    banco = myc.connect(
        host="127.0.0.1",
        porta=3307,
        user="",
        password="",
        database="biblioteca"
    )
    
    cursor = banco.cursor()
    return banco,cursor

# função para cadastrar os dados do bibliotecario
def cadastrar(nome, email, telefone):
    banco,cursor = conectar_banco()
    # variável para inserir os dados na tabela 
    sql = "INSERT INTO bibliotecario(nome,email,telefone)VALUES(%s,%s,%s)"
    # passando os valores para os parâmetros %s
    val = (nome,email,telefone)
    # vamos executar a consulta
    cursor.execute(sql,val)
    # confirmar a excução da consulta
    banco.commit()
    # fechar cursor
    cursor.close()
    # fechar banco
    banco.close()

# função para selecionar os dados
def listar_bibliotecarios():
    banco,cursor = conectar_banco()
    # variavel para guardar o retorno do select
    sql = "SELECT * FROM bibliotecario"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]}")

    # fechar cursor
    cursor.close()
    # fechar o banco
    banco.close()

# função para realizar a atualização dos dados
def atualizar_bibliotecario(id,nome,email,telefone):
    banco,cursor = conectar_banco()
    sql = "UPDATE usuarios SET nome = %s, email = %s, telefone = %s WHERE id_bibliotecario = %s"
    val = (nome,email,telefone,id)
    cursor.execute(atualizar_bibliotecario,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados atualizados")

    # apagar o bibliotecario
    def apagar_bibliotecario(id):
        banco, cursor =conectar_banco()
        sql = "DELETE FROM bibliotecario WHERE id_bibliotecario = %s"
        val = (id)
        cursor.execute(sql, val)
        banco.commit()
        cursor.close()
        banco.close()
        print("bibliotecario deletado")