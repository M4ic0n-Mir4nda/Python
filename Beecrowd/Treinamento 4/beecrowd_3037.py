def jogo_dardos(pontuacoes):
    for _ in range(qtd_jogos):
        joao = 0
        maria = 0
        for j in range(3):
            pontuacao, distancia = input().split()
            pontuacao = int(pontuacao)
            distancia = int(distancia)
            soma = pontuacao * distancia
            joao += soma
        for m in range(3):
            pontuacao, distancia = input().split()
            pontuacao = int(pontuacao)
            distancia = int(distancia)
            soma = pontuacao * distancia
            maria += soma
        if maria > joao:
            print('MARIA')
        else:
            print('JOAO')

qtd_jogos = int(input())
jogo_dardos(qtd_jogos)
