for T in range(int(input())):
    a = input().strip().split()
    # print(a)
    cont = 0
    for i in range(int(a[0]),int(a[1])+1):
        if a[-1] in str(i):
            cont += 1
    print(cont)