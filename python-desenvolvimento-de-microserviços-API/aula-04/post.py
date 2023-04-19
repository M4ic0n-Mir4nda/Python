from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/v1/aula/cadastrar', methods=["POST"])
def cadastrar():
     input_json = request.get_json(force=True) 
     #camada de banco de dados
     jsonToReturn = {'nome':input_json['nome'], 'Cadastro':'Para efetuar o cadastro passe o seu código'}
     return jsonify(jsonToReturn), 401


@app.route('/v1/aula/consultar', methods=["GET"])
def consultar():
    #return jsonify(list(range(5)))
    return 'primeira chamada de api!'
