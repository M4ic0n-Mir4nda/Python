from flask import Flask, request, jsonify
import json

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'name': "task1",
        "description": "This is task 1"
    },
    {
        "id": 2,
        "name": "task2",
        "description": "This is task 2"
    },
    {
        "id": 3,
        "name": "task3",
        "description": "This is task 3"
    }
]

tasksJSON = json.dumps(tasks)


@app.route('/')
def home():
    return "App Works!!!"

@app.route('/v1/aula/cadastrar', methods=["POST"])
def cadastrar():
     input_json = request.get_json(force=True) 
     #camada de banco de dados
     jsonToReturn = {'nome':input_json['nome'], 'Cadastro':'Para efetuar o cadastro passe o seu código'}
     return jsonify(jsonToReturn), 401


@app.route('/api/tasks')
def tasks():
    return tasksJSON


if __name__ == '__main__':
    app.run()