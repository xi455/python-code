for T in range(int(input())):
    val = input().strip().split()

    for i in range(len(val)):
        val[i] = val[i].split(',')

    for i in range(len(val)):
        val[i][2] = int(val[i][2])

    val.sort(key=lambda val: val[2])
    for i in range(len(val)):
        val[i][2] = str(val[i][2])

    val_alpha_set = []
    val_alpha_any = []
    val_num = []

    for i in range(len(val)):
        val_alpha = []
        for j in range(len(val[i])):
            if val[i][j].isalpha() == True:
                if val[i][j] not in val_alpha_set:
                    val_alpha_set.append(val[i][j])
                val_alpha.append(val[i][j])

        val_alpha_any.append(val_alpha)

    val_num_is = [i for i in range(len(val_alpha_set))]
    val_num_dict = dict()
    for i in val_num_is:
        val_num_dict[i] = i

    def Find(k):
        if val_num_dict[k] == k:
            return k
        else:
            return Find(val_num_dict[k])

    def Union(a, b):
        x = Find(a)
        y = Find(b)

        val_num_dict[y] = x
        if x != y:
            return True

    cont = 0
    for i in range(len(val_alpha_any)):
        bool = Union(val_alpha_set.index(
            val_alpha_any[i][0]), val_alpha_set.index(val_alpha_any[i][1]))
        if bool:
            cont += int(val[i][2])

    print(cont)
