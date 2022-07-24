n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {media:.1f}')
if media >= 7.0:
    print('Aluno aprovado.')
elif media < 5.0:
    print('Aluno reprovado.')
else:
    if media >= 5.0 and media <= 6.9:
        print('Aluno em exame.')
        nota_exame = float(input())
        print(f'Nota do exame: {nota_exame:.1f}')
        nova_media = (media + nota_exame) / 2
        if media >= 5.0:
            print('Aluno aprovado.')
            print(f'Media final: {nova_media:.1f}')
        else:
            print('Aluno reprovado.')


