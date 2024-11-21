import mysql.connector as myc 

def conectar_banco():
    banco = myc.connect(
        host="127.0.0.1",
        porta=3307,
        user="",
        password="",
        database="emprestimo"
    )

    cursor = banco.cursor()
    return banco,cursor

# cadastrar emprestimo
def cadastrar(data_devolucao_prevista, data_devolucao_real):
    banco,cursor = conectar_banco()
    sql = "INSERT INTO imprestimo(data_devolucao_prevista, data_devolucao_real, id_publicacao, id_aluno, id_bibliotecario)VALUES(%s,%s,%s,%s,%s)"
    val = ()
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()

# selecionar dados do emprestimo
def listar_emprestimo():
    banco,cursor = conectar_banco()
    sql = "SELECT * FROM imprestimo"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]} - {i[6]}")

    cursor.close()
    banco.close()  

# atualizar emprestimo
def atualizar_emprestimo(id, data_devolucao_real):
    banco,cursor = conectar_banco()
    sql = "UPDATE emprestimo SET nome = data_devolucao_real = %s WHERE id_emprestimo = %s"
    val = (data_devolucao_real,id)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados do emprestimo atualizados")

    # apagar emprestimo
    def apagar_emprestimo(id):
        banco, cursor =conectar_banco()
        sql = "DELETE FROM emprestimo WHERE id_emprestimo = %s"
        val = (id)
        cursor.execute(sql, val)
        banco.commit()
        cursor.close()
        banco.close()
        print("Emprestimo deletado")