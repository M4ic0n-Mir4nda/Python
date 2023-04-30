from mysql.connector import Error
import mysql.connector
from flask import Flask, jsonify, request, redirect, url_for

class ConnDB:
    def __init__(self, host = 'localhost', database = 'db_alunos', user = 'root', password = 'root'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def conecta(self):
        self.con = mysql.connector.connect(
            host = self.host,
            database = self.database,
            user = self.user,
            password = self.password
        )
        self.cur = self.con.cursor()

    def commit(self):
        if self.fetchone():
            pass
        self.con.commit()

    def desconecta(self):
        self.con.close()
    
    def executeQuery(self, query, dado = ''):
        self.conecta()
        self.cur.execute(query, dado)
        res = self.fetchall()
        self.commit()
        self.desconecta()
        return res

    def fetchall(self):
        return self.cur.fetchall()

    def fetchone(self):
        return self.cur.fetchone()

app = Flask(__name__)
con = ConnDB()

@app.route('/')
def main():
    return 'Aplicação Iniciada!'

@app.route('/alunos', methods=["GET"])
def getAllAlunos():
    try:
        con.conecta()
        arrAlunos = []
        query_sql = 'SELECT * FROM Alunos'
        linhas = con.executeQuery(query_sql)
        for linha in linhas:
            aluno = {
                "id": linha[0],
                "nome": linha[1],
                "idade": linha[2],
                "turma": linha[3]
            }
            arrAlunos.append(aluno)
        return jsonify(arrAlunos), 200
    except Error as err:
        return f'Ocorreu um erro, {err}', 500

@app.route('/aluno/<int:id>', methods=["GET"])
def getAluno(id):
    try:
        con.conecta()
        query_sql = f'SELECT * FROM Alunos WHERE id={id}'
        colunas = con.executeQuery(query_sql)
        for coluna in colunas:
            aluno = {
                "id": coluna[0],
                "nome": coluna[1],
                "idade": coluna[2],
                "turma": coluna[3],
            }
        return jsonify(aluno), 200
    except Error as err:
        return f'Ocorreu um erro, {err}', 500

@app.route('/alunos', methods=["POST"])
def createAluno():
        con.conecta()
        try:
            if request.method == 'POST':
                content = request.get_json()
                query_sql = 'INSERT INTO Alunos (nome, idade, turma) VALUES (%s,%s,%s)'
                data = (content['nome'], content['idade'], content['turma'])
                con.executeQuery(query_sql, data)
                return redirect(url_for('getAllAlunos'))
        except Error as err:
            return f'Ocorreu um erro, {err}', 500

@app.route('/aluno/<int:id>', methods=["DELETE"])
def deleteAluno(id):
    try:
        con.conecta()
        query_sql = f'DELETE FROM Alunos WHERE id={id}'
        con.executeQuery(query_sql)
        return f'Aluno {id} excluido'
    except Error as err:
        return f'Ocorreu um erro, {err}', 500

app.run(debug=True)