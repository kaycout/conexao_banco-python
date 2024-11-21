import mysql.connector as myc 

def conectar_banco():
    banco = myc.connect(
        host="127.0.0.1",
        porta=3307,
        user="",
        password="",
        database="publicacao"
    )

    cursor = banco.cursor()
    return banco,cursor

# cadastrar publicacao
def cadastrar(titulo, autor, editora, data_publicacao, isbn, assunto, tipo_publicacao, palavras_chave, quantidade, localizacao):
    banco,cursor = conectar_banco()
    sql = "INSERT INTO publicacao(titulo, autor, editora, data_publicacao, isbn, assunto, tipo_publicacao, palavras_chave, quantidade, localizacao)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (titulo, autor, editora, data_publicacao, isbn, assunto, tipo_publicacao, palavras_chave, quantidade, localizacao)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()

# selecionar dados da publicacao 
def listar_publicacao():
    banco,cursor = conectar_banco()
    sql = "SELECT * FROM publicacao"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}  - {i[5]}  - {i[6]} - {i[7]} - {i[8]} - {i[9]} - {i[10]}")

    cursor.close()
    banco.close()  

# atualizar publicacao
def atualizar_publicacao(id, titulo, autor, editora, data_publicacao, isbn, assunto, tipo_publicacao, palavras_chave, quantidade, localizacao):
    banco,cursor = conectar_banco()
    sql = "UPDATE publicacao SET nome = %s, titulo = %s, autor = %s, editora = %s, data_publicacao = %s, isbn = %s, assunto = %s, tipo_publicacao = %s,  palavras_chave = %s, quantidade %s, localizacao = %s WHERE id_publicacao = %s"
    val = (titulo, autor, editora, data_publicacao, isbn, assunto, tipo_publicacao, palavras_chave, quantidade, localizacao, id)
    cursor.execute(atualizar_publicacao,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados da publicacao atualizados")

    # apagar publicacao
    def apagar_publicacao(id):
        banco, cursor =conectar_banco()
        sql = "DELETE FROM publicacao WHERE id_publicacao = %s"
        val = (id)
        cursor.execute(sql, val)
        banco.commit()
        cursor.close()
        banco.close()
        print("Publicação deletada")