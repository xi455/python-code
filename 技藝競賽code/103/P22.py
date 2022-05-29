for T in range(int(input())):
    val_1 = input().strip().split()[1:]
    val_2 = input().strip().split()[1:]
 
    val_set = set()
    for i in range(len(val_1)):
        if val_1[i] in val_2:
            val_set.add(val_1[i])
    print(len(val_set))
