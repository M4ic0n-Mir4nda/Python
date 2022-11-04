from flask import Flask, render_template, redirect, request, session, url_for

class Produto:
    def __init__(self, descricao, quantidade, valor):
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

usuarios = ['maicon', 'lucas', 'larissa']
lista_produtos = []

app = Flask(__name__)
app.secret_key = 'teste'

@app.route('/')
def index():
    return render_template('index.html', produtos=lista_produtos)

@app.route('/novo')
def novo():
    if 'logado' not in session or session['logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('novo.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    descricao = request.form['desc']
    quantidade = request.form['qtd']
    valor = request.form['valor']
    produto = Produto(descricao, int(quantidade), float(valor.format(';', '.')))
    lista_produtos.append(produto)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('form.html')

@app.route('/validar', methods=['GET', 'POST'])
def validar():
    if request.method == 'POST':
        if request.form['name'] in usuarios:
            session['logado'] = request.form['name']
            return redirect('/') 
        else:
            return redirect('/login')

@app.route('/logout')
def logout():
    session['logado'] = None
    return redirect(url_for('index'))

app.run(debug=True)