a = [[n*m for m in range(-10, 10)] for n in range(-10, 10)]

for n in range(-10, 10):
    row = ''
    for m in range(-10, 10):
        cell = a[n][m]
        cell_formated = f'{cell: >3}'
        if row:
            row = row + '. '
        row = row + cell_formated
    print(row)
