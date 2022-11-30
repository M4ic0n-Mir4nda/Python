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

class Produto:
    def __init__(self, codigo, descricao, quantidade, valor):
        self.codigo = codigo
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

prod1 = Produto(12563, 'Arroz 5kg', 50, 15.22)
prod2 = Produto(52369, 'Bolacha trakinas', 31, 2.99)
lista_prod = [prod1, prod2]

@app.route('/')
def index():
    try:
        consulta = """select codigo, descricao, quantidade, valor from PRODUTO"""
        cursor.execute(consulta)
        data = cursor.fetchall()
        for row in data:
            return render_template('index.html', 
                titulo='Produtos',
                produtos=data)
        cursor.close()
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
        produto = Produto(codigo, descricao, quantidade, valor)
        cadastro_prod = f"""INSERT INTO PRODUTO 
                            (CODIGO, DESCRICAO, QUANTIDADE, VALOR)
                            VALUES
                            ('{codigo}', '{descricao}', {quantidade}, {valor})
                        """
        cursor.execute(cadastro_prod)
        cursor.commit()
        lista_prod.append(produto)
        return redirect(url_for('index'))

app.run(debug=True)
