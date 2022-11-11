def retorna_nome(lista, indice):
    try:
        for i in range(len(lista)):
            return lista[indice]
    except IndexError:
        return 'Indice não existe na lista'

print(retorna_nome(['Joao', 'Maicon', 'Lucas', 'Larrisa', 'Juliana'], 10))
print(retorna_nome(['Joao', 'Maicon', 'Lucas', 'Larrisa', 'Juliana'], 1))