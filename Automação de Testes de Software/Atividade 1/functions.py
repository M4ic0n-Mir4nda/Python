def calcula_salario_liquido(valorHoraAula, numAulas, INSS):
    salario_bruto = valorHoraAula * numAulas
    return round(salario_bruto - (salario_bruto * INSS / 100), 2)

def calcula_desconto(valorProd):
    desconto = valorProd * 9 / 100
    return round(valorProd - desconto), round(desconto)

def calcula_desconto_reais(valorOriginal, valorDesconto):
    return round(valorOriginal - valorDesconto, 2)

def calcula_gorjeta(valor):
    adicional = valor * 10 / 100
    return round(valor + adicional, 2), round(adicional, 2)
