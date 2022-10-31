Lista = []
while True:
    n = int(input())
    if n > 0:
        Lista.append(n)
        media = sum(Lista) / len(Lista)
    else:
        print(f'MEDIA: {media:.2f}')
        for i in range(len(Lista)):
            if Lista[i] < media:
                print(Lista[i])
        break
