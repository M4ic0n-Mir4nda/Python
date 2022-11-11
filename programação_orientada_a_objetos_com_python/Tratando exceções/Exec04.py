alunos = {}
for i in range(2):
    try:
        ra = input('RA: ')
        if len(ra) != 7:
            raise ValueError
        elif ra in alunos:
            raise TypeError
        else:
            nome = input('Qual seu nome? ')
            alunos[ra] = nome
    except ValueError:
        print('RA incorreto')
    except TypeError:
        print('RA já existe no cadastro')

print(alunos)