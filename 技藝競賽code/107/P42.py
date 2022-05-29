for T in range(int(input())):
    val = input().strip().replace('[', '').replace(']', '').split(', ')
    val = list(map(int, val))
    val.insert(0, 0)

    val_c = []
    val_any = []
    for i in range(1, len(val)):
        if i not in val_c:
            val_c.append(i)
        else:
            continue

        val_list = []
        k = i
        val_list.append(k)

        while k != val[i] and val[i] not in val_list:
            val_list.append(val[i])
            val_c.append(val[i])
            k = val[i]
            i = k
        val_any.append(val_list)
    print(val_any)
