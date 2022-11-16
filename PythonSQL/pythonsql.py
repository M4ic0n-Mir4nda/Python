import pyodbc

#hostname no cmd

#Dados da conexao no banco
dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-E9ARPQB;"
    "Database=PythonSQL;"
)

#Cria a conexao com o banco de dados
conexao = pyodbc.connect(dados_conexao)
print('Conexão bem Sucedida')

#Variavel criada para executar os comandos no banco
cursor = conexao.cursor()

id = 3
cliente = 'Maicon Python'
produto = 'Carro'
data = '15/12/2022'
preco = '5000'
quantidade = 1

comando = f"""INSERT INTO VENDAS
(ID_VENDA, CLIENTE, PRODUTO, DATA_VENDA, PRECO, QUANTIDADE)
VALUES
({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})"""

cursor.execute(comando)
cursor.commit()