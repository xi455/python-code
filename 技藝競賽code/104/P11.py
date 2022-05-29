for T in range(int(input())):
    row_num = int(input())
    val = [int(i) for i in input().strip().split(',')]
    cont = 0
    for i in range(1,row_num):
        if val[i] > val[i-1]:
            cont += (val[i] - val[i-1]) * 20
        else:
            cont += (val[i-1] - val[i]) * 10
    print(cont)
