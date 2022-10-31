def carrinho(compra):
    for item in escolha:
        if item != "":
            lista.append(int(item))
        else:
            break
    return lista

def adicionar(opcao):
    n = int(escolha[1])
    lista.append(n)

def exibir(lista):
    lista.sort(key=int)
    print(*lista)

def remover(opcao, lista):
    n = int(escolha[1])
    busca_prod = n in lista
    if busca_prod == True:
        lista.remove(n)
    else:
        print(f'código {n} não encontrado')

def encerrar(compra):
    lista.sort(key=int)
    print(*lista)

lista = []

while True:
    escolha = input().split(' ')
    acao = (escolha[0])
    if acao == 'adicionar':
        adicionar(escolha)
    elif acao == 'remover':
        remover(escolha, lista)
    elif acao == 'exibir':
        exibir(lista)
    elif acao == 'encerrar':
        encerrar(escolha)
        break
    else:
        carrinho(escolha)