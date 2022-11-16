import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server={DESKTOP-E9ARPQB};"
    "Database=PythonSQL;"
)

conexao = pyodbc.connect(dados_conexao)
if conexao:
    print('Conexao bem sucedida')
else:
    print('Erro')

cursor = conexao.cursor()

while True:
    acao = input('Qual ação você quer fazer? ')
    if acao == 'cadastro':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        email = input('Digite seu e-mail: ')
        comando = f"""INSERT INTO USUARIO
                    (NOME, IDADE, EMAIL)
                    VALUES
                    ('{nome}', {idade}, '{email}')"""
        cursor.execute(comando)
        cursor.commit()
        print('Cadastro efetuado com sucesso')
    elif acao == 'buscar':
        user = input('Qual é o nome do usuario que você quer consultar: ')
        cursor.execute(f" SELECT NOME, IDADE FROM USUARIO WHERE NOME LIKE '%{user}%' ")
        for nome in cursor:
            print(f'Usúario:{nome}')
    else:
        cursor.execute("SELECT * FROM USUARIO")
        for user in cursor:
            print(user)
    



