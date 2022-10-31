from produto import Produto
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/produtos')
def produtos():
    prod1 = Produto('ABC', 'XZ123', 8000, 6)
    prod2 = Produto('Xyz', 'Mobile3', 3500, 30)
    prod3 = Produto('TecVision', 'Lv5000', 6000, 85)
    lista = [prod1, prod2, prod3]
    return render_template('produtos.html', lista_produtos=lista)

app.run(debug=True)