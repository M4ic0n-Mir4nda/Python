from mysql.connector import Error
import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return 'Aplicação Iniciada!'

@app.route('/alunos', methods=["GET"])
def listarAlunos():
    con = mysql.connector.connect(host='localhost',database='db_alunos',user='root',password='root')
    try:
        arrAlunos = []
        cursor = con.cursor()
        busca_alunos = 'select * from Alunos'
        cursor.execute(busca_alunos)
        linhas = cursor.fetchall()
        for linha in linhas:
            aluno = {
                "id": linha[0],
                "nome": linha[1],
                "idade": linha[2],
                "turma": linha[3]
            }
            arrAlunos.append(aluno)
    except Error as err:
        return f'Ocorreu um erro, {err}'
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
        return jsonify(arrAlunos), 200

app.run(debug=True)