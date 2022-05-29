for T in range(int(input())):
    val_any = [i.split(',') for i in input().strip().split()]

    val_li = []
    for i in range(len(val_any)):
        for j in range(len(val_any[i])):

            if val_any[i][j] not in val_li:
                val_li.append(val_any[i][j])

    if len(val_li) - len(val_any) > 1:
        print('F')
        continue

    val_arr = [[val_li[i]] for i in range(len(val_li))]

    for i in range(len(val_any)):
        for j in range(len(val_arr)):
            if val_arr[j][0] in val_any[i]:
                for k in range(len(val_any[i])):
                    if val_any[i][k] not in val_arr[j]:
                        val_arr[j].append(val_any[i][k])

    val_lll = []

    def val_fn(ii, val_list=[]):
        for i in range(1, len(val_arr[ii])):
            for j in range(len(val_any)):

                val_ll = []
                if val_arr[j][0] == val_arr[ii][i]:
                    val_ll.append(val_arr[ii][0])
                    val_ll.append(val_arr[ii][i])

                    if val_arr[ii][i] not in val_list:
                        val_lll.append(val_ll)
                        boo = val_fn(j, val_list+[val_arr[ii][i]])

                        if boo:
                            return True

                    else:
                        if val_ll[::-1] not in val_lll:
                            an = val_list[val_list.index(val_arr[ii][i]):]
                            an = list(map(int, an))
                            an.sort()
                            an = list(map(str, an))
                            print(', '.join(an))
                            return True

                        else:
                            break

    boo = val_fn(0, val_list=[val_arr[0][0]])
    if boo != True:
        print('T')
