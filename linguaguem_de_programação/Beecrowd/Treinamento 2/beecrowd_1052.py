meses = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
a = int(input())
print(meses[a])

meses = int(input())

if meses == 1:
    print('January')
elif meses == 2:
    print('February')
elif meses == 3:
    print('March')
elif meses == 4:
    print('April')
elif meses == 5:
    print('May')
elif meses == 6:
    print('June')
elif meses == 7:
    print('July')
elif meses == 8:
    print('August')
elif meses == 9:
    print('September')
elif meses == 10:
    print('October')
elif meses == 11:
    print('November')
else:
    print('December')
