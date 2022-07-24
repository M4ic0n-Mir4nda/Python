numero_testes = int(input())
for teste in range(numero_testes):
    n = int(input())
    for caso_teste in range(n):
        feedback = int(input())
        if feedback == 1:
            print('Rolien')
        elif feedback == 2:
            print('Naej')
        elif feedback == 3:
            print('Elehcim')
        else:
            print('Odranoel')