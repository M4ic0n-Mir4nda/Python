nota_trabalhos = float(input())
nota_prova = float(input())
media_final = (nota_trabalhos + nota_prova) / 2
if media_final >= 6:
    print('aprovado')
else:
    if media_final < 6:
        subtitutiva = 10
        nova_media = (nota_trabalhos + subtitutiva) / 2
        if nova_media >= 6:
            print('talvez com a sub')
        else:
            print('reprovado')
