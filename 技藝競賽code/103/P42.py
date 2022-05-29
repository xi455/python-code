for T in range(int(input())):
    value = [int(i) for i in input().strip().split(',')]

    value_arr = [[int(i) for i in input().strip().split()]
                 for j in range(value[0])]

    for i in range(len(value_arr)):
        value_arr[i] = value_arr[i][1:]

    val_an = []
    for i in range(value[1]):
        cont = 0
        val = value_arr[value[2]][i]
        while val != 999:
            val = value_arr[val][i]
            cont += 1
        val_an.append(str(cont))
    print(','.join(val_an))
