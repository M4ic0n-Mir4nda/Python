nome = str(input())
salario = float(input())
vendas = float(input())
comissao = (vendas * 0.15) + salario
print('TOTAL = R$ {:.2f}'.format(comissao))
