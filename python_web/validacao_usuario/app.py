from flask import Flask, render_template, redirect, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, select, update, values
# https://www.javatpoint.com/flask-sqlalchemy base SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///loja.sqlite3'
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

lista_produtos = []
admin = ['maicon']

class Usuario(db.Model):
    id = db.Column('ID_USUARIO', db.Integer, primary_key=True)
    usuario = db.Column(db.String(255), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

class Produto(db.Model):
    id = db.Column('ID', db.Integer, primary_key=True)
    descricao = db.Column(db.String(255))
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float(50))

    def __init__(self, descricao, quantidade, valor):
        self.descricao = descricao
        self.quantidade = quantidade
        self.valor = valor

@app.route('/')
def index():
    return render_template('index.html', produtos=Produto.query.all())

@app.route('/novo')
def novo():
    if 'logado' not in session or session['logado'] == None:
        return redirect(url_for('login'))
    else:
        return render_template('novo.html')

@app.route('/estoque')
def estoque():
    return render_template('delete.html', produtos=Produto.query.all())

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        #prod = request.form.get('produto.id')
        obj = Produto.query.filter_by(id == 1)
        db.session.delete(obj)
        db.session.commit()
        return redirect(url_for('index'))

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    #produto = Produto(request.form['desc'], request.form['qtd'], request.form['valor'])
    descricao = request.form['desc']
    quantidade = request.form['qtd']
    valor = request.form['valor']
    produto = Produto(descricao, int(quantidade), float(valor.replace(',','.')))
    db.session.add(produto)
    db.session.commit()
    lista_produtos.append(produto)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('form.html')

@app.route('/validar', methods=['GET', 'POST'])
def validar():
    if request.method == 'POST':
        if request.form['name'] in admin:
            session['logado'] = request.form['name']
            return render_template('novo.html')
    else:
        return redirect(url_for('login.html'))

@app.route('/logout')
def logout():
    session['logado'] = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)