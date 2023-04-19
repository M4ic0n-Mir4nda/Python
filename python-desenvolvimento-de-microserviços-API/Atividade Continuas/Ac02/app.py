from flask import Flask, jsonify

# Maicon Miranda - RA: 2200966

app = Flask(__name__)

listProducts = [
    {
        "id": "1",
        "name": "product 1"
    },
    {
        "id": "2",
        "name": "product 2"
    },
    {
        "id": "3",
        "name": "product 3"
    }
]

@app.route('/', methods=["GET"])
def main():
    return 'Página Inicial'

@app.route('/produtos', methods=["GET"])
def products():
    return jsonify(listProducts)

@app.route('/produtos/<int:id>/', methods=["GET"])
def product(id):
    try:
        if id == 0:
            return jsonify('Error: id não existe'), 500
        item = [
            f'id: {listProducts[id - 1]["id"]}',
            f'name: {listProducts[id - 1]["name"]}'
        ]
        return jsonify(item), 200
    except:
        return jsonify('Error: id não existe'), 500

app.run(debug=True)