for T in range(int(input())):
    val_1 = [i for i in input().strip()]
    val_2 = [i for i in input().strip()]
 
    val_set = set()
    for i in range(len(val_1)):
        if val_1[i] in val_2:
            val_set.add(val_1[i])
 
    val_list = sorted(val_set)
    if val_list != []:
        print(''.join(val_list))
    else:
        print('N')
