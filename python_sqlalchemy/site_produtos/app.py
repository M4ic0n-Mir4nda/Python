from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, redirect, url_for, request

'''
https://www.digitalocean.com/community/tutorials/how-to-use-one-to-many-database-relationships-with-flask-sqlalchemy

import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
           'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
'''
engine = create_engine("sqlite:///server.db")
connection = engine.connect()

session = Session()

Base = declarative_base(engine)

connection.execute("""CREATE TABLE IF NOT EXISTS PRODUTO (
                        ID_PRODUTO INTEGER PRIMARY KEY,
                        DESCRICAO VARCHAR(255),
                        QUANTIDADE INT,
                        VALOR FLOAT)
                    """)

app = Flask(__name__)

class Produto(Base):
    __tablename__ = 'PRODUTO'
    id = Column('ID_PRODUTO', Integer, primary_key=True, autoincrement=True)
    descricao = Column('DESCRICAO', String(255))
    qtd = Column('QUANTIDADE', Integer)
    valor = Column('VALOR', Float)

    def __init__(self, descricao, qtd, valor):
        self.descricao = descricao
        self.qtd = qtd
        self.valor = valor

prod1 = Produto('Arroz 5kg', 50, 15.22)
prod2 = Produto('Bolacha trakinas', 31, 2.99)
lista_prod = [prod1, prod2]

@app.route('/')
def index():
    return render_template('index.html', titulo='Produtos', produtos=lista_prod)

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        produto = Produto(
            request.form['descricao'],
            request.form['quantidade'],
            request.form['valor'])
        session.add(produto)
        session.commit()
        #lista_prod.append(produto) Erro ao adicionar a lista na 2° vez e retornar a view para o usúario
        return redirect(url_for('index'))

app.run(debug=True)
