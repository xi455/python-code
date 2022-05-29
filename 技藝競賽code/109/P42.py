for T in range(int(input())):
    row = int(input())
    val_bool = [False] * (row + 1)
    val_list = [0] * (row + 1)
    for i in range(row):
        val = input().strip().split()
        val = list(map(int,val))
        val_list[val[0]] = val[1]
 
    num_max = 0
    num_k = 0
    for i in range(1,row + 1):
        if val_bool[i] == True:
            continue
        k = i
        num = 0
        val_bool_bool = [False] * (row + 1)
        while not val_bool_bool[k]:
            val_bool_bool[k] = True
            val_bool[k] = True
            k = val_list[k]
            num += 1
        if num > num_max:
            num_k = i
            num_max = num
    print(num_k)