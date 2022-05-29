for T in range(int(input())):
    val = [int(i) for i in input().strip().split(',')]
    bool = True
    for i in val:
        for j in range(9,1,-1):
            if i == j: continue
            if i % j == 0:
                bool = False
                break
        if bool == False:
            break
    if bool == True and abs(val[-1] - val[0]) == 2:
        print('Y')
    else:
        print('N')
