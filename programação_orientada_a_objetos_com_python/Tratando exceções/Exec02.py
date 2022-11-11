def funcao_1():
    print('Inicio da função')
    lista = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
    for i in range(15):
        try:
            print(lista[i])
        except IndexError:
            print('Erro ao percorrer lista')
            break
    print('Fim da função')

print('Inicio do programa')
funcao_1()
print('Fim do programa')