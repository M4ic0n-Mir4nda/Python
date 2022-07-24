while True:
    try:
        epr = 0
        ehd = 0
        intrusos = 0
        n = int(input())
        for i in range(n):
            matricula, curso = input().split()
            if curso == 'EPR':
                epr += 1
            elif curso == 'EHD':
                ehd += 1
            else:
                intrusos += 1
        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intrusos}')
    except:
        break