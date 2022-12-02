import pyodbc
from flask import Flask, render_template, redirect, url_for, request

dados_conexao = (
    "Driver={SQL Server};"
    "Server={DESKTOP-E9ARPQB};"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão bem Sucedida')

cursor = conexao.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    try:
        consulta = """select codigo, descricao, quantidade, valor from PRODUTO"""
        descricao = """SELECT DESCRICAO FROM PRODUTO"""
        quantidade = """SELECT QUANTIDADE FROM PRODUTO"""
        valor = """SELECT VALOR FROM PRODUTO"""
        cursor.execute(consulta)
        data = cursor.fetchall()
        for row in data:
            pass
        cursor.execute(descricao)
        desc = cursor.fetchall()
        for row in desc:
            pass
        cursor.execute(quantidade)
        qtd = cursor.fetchall()
        for row in qtd:
            pass
        cursor.execute(valor)
        val = cursor.fetchall()
        for row in val:
            pass
        return render_template('index.html', titulo='Produtos', produtos=data, descricao=desc, quantidade=qtd, valor=val)
    except Exception:
        return 'Erro ao carregar dados'

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        quantidade = request.form['quantidade']
        valor = request.form['valor']
        cadastro_prod = f"""INSERT INTO PRODUTO 
                            (CODIGO, DESCRICAO, QUANTIDADE, VALOR)
                            VALUES
                            ('{codigo}', '{descricao}', {quantidade}, {valor})
                        """
        cursor.execute(cadastro_prod)
        cursor.commit()
        return redirect(url_for('index'))

app.run(debug=True)