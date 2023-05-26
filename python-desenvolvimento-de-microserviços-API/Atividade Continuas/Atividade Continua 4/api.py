from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def main():
    return 'Aplicação Iniciada!'

@app.route('/api/get', methods=["GET"])
def getAPI():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(api_url)
    return response.json()

@app.route('/api/post', methods=["POST"])
def postAPI():
    api_url = "https://jsonplaceholder.typicode.com/todos"
    content = {"userId": 1, "title": "Teste API", "completed": False}
    response = requests.post(api_url, json=content)
    return response.json()

@app.route('/api/delete', methods=["DELETE"])
def deleteAPI():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(api_url)
    return response.json()

app.run(debug=True)