# INSIRA ABAIXO OS NOMES DOS ALUNOS DO GRUPO (máximo 6 alunos)
# ALUNO 1: Maicon Miranda Santana

'''
Escreva uma função com o nome 'pertence', que recebe como argumentos de entrada
uma lista e três itens e retorna 1, se os três itens estiverem armazenados
na lista, e 0 caso contrário.
'''


def pertence(lista, item1, item2, item3):
    resultado = 0
    for verificar in lista:
        if item1 in lista and item2 in lista and item3 in lista:
            resultado = 1
    return resultado


'''
Escreva uma função chamada 'substituir' que recebe como argumentos de entrada
uma tupla e dois itens (velho e novo) e retorna uma tupla onde todas as
ocorrências do item velho são substituídas pelo item novo.
'''


def substituir(tupla, velho, novo):
    lista = []
    for i in range(len(tupla)):
        if velho == tupla[i]:
            temp = velho
            velho = novo
            lista.append(velho)
            velho = temp
        else:
            lista.append(tupla[i])
    resultado = tuple(lista)
    return resultado


'''
Escreva uma função chamada 'posicoes' que recebe como argumentos de entrada
uma tupla e um item, e retorna uma lista contendo todos os índices em que o
item aparece na tupla.
Caso o item nao exista na tupla, deve retornar uma lista vazia.
'''


def posicoes(tupla, item):
    resultado = []
    for pos in range(len(tupla)):
        if tupla[pos] == item:
            indice = pos
            resultado.append(indice)
    return resultado


'''
Considere um dicionario onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'reprovados' que recebe como argumentos
de entrada o dicionário e retorna uma lista com o nome dos alunos reprovados.
A lista de nomes deve ser ordenada em ordem alfabética.
Caso nenhum aluno seja reprovado, deve retornar uma lista vazia.
Considere que o aluno é reprovado se a média das suas notas é inferior a 6.
'''


def reprovados(alunos):
    reprovados = []
    for i in alunos:
        soma = 0
        media = 0
        for j in range(len(alunos[i])):
            nota = alunos[i][j]
            soma += nota
        media = soma / len(alunos[i])
        if media < 6:
            reprovados.append(i)
    reprovados.sort()
    return reprovados


'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'excluir_nota' que recebe como argumentos
de entrada o dicionário, o nome de um aluno e uma nota.
A função deve excluir todas as ocorrências dessa nota do aluno informado e
retornar o dicionário com as alterações realizadas.
Se aluno não estiver no dicionário, deve retornar o dicionário sem alterações.
'''


def excluir_nota(alunos, nome, nota):
    lista = {}
    for i in alunos:
        notas = []
        for j in range(len(alunos[i])):
            if nota == alunos[i][j] and i == nome:
                continue
            else:
                t = alunos[i][j]
                notas.append(t)
        aluno = i
        lista[aluno] = notas
    alunos = lista
    return alunos



'''
Considere um dicionário onde a chave é o nome de um aluno e o valor uma lista
de notas. Escreva uma função chamada 'menor_nota' que recebe como argumentos
de entrada o dicionário e retorna outro dicionário com o nome e a menor nota
de cada aluno.
'''


def menor_nota(alunos):
    lista = {}
    for nome in alunos:
        menor = 0
        for nota in range(len(alunos[nome])):
            maior = alunos[nome][nota]
            if menor > maior:
                aluno = nome
                lista[aluno] = maior
            menor = alunos[nome][nota]
    alunos = lista
    return alunos

