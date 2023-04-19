from flask import Flask;

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    Numero = 6
    if Numero % 2 == 0:
        return f'É par: {Numero}'
    return 'Não é par'
        
app.run(debug=True)