row = int(input())
bingo = input().strip().split(',')
for T in range(row):
    two = three = four = five = 0
    val = input().strip().split(',')
    for i in range(len(val)):
        cont = 0
        for j in range(len(val)):
            if val[i] == val[j]:
                continue
            if val[j] in bingo:
                cont += 1
        if cont == 2:
            two += 1
        elif cont == 3:
            three += 1
        elif cont == 4:
            four += 1
        elif cont == 5:
            five += 1
    print('{},{},{},{}'.format(two,three,four,five))
