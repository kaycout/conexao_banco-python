import mysql.connector as myc 

def conectar_banco():
    banco = myc.connect(
        host="127.0.0.1",
        porta=3307,
        user="",
        password="",
        database="aluno"
    )

    cursor = banco.cursor()
    return banco,cursor

# cadastrar aluno
def cadastrar(nome, matricula, curso, email, telefone):
    banco,cursor = conectar_banco()
    sql = "INSERT INTO aluno(nome,matricula,curso,email,telefone)VALUES(%s,%s,%s,%s,%s)"
    val = (nome, matricula, curso, email, telefone)
    cursor.execute(sql,val)
    banco.commit()
    cursor.close()
    banco.close()

# selecionar dados do aluno
def listar_alunos():
    banco,cursor = conectar_banco()
    sql = "SELECT * FROM aluno"
    cursor.execute(sql)
    resultado = cursor.fetchall()
    for i in resultado:
        print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]}  - {i[5]}  - {i[6]} - {i[7]}")

    cursor.close()
    banco.close()  

# atualizar aluno
def atualizar_aluno(id, nome, matricula, curso, email, telefone):
    banco,cursor = conectar_banco()
    sql = "UPDATE aluno SET nome = %s, matricula = %s, curso, email = %s, telefone = %s WHERE id_aluno = %s"
    val = (nome, matricula, curso, email, telefone, id)
    cursor.execute(atualizar_aluno,val)
    banco.commit()
    cursor.close()
    banco.close()
    print("Dados do aluno atualizados")

    # apagar aluno
    def apagar_aluno(id):
        banco, cursor =conectar_banco()
        sql = "DELETE FROM aluno WHERE id_aluno = %s"
        val = (id)
        cursor.execute(sql, val)
        banco.commit()
        cursor.close()
        banco.close()
        print("Aluno deletado")



