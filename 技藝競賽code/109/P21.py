for T in range(int(input())):
    a = list(map(int,input().strip().split('/')))
    b = list(map(int,input().strip().split('/')))
    # print(a,b)
    k = a[-1] - b[-1]
    if a[1] < b[1]:
        k -= 1
    elif a[1] == b[1]:
        if a[0] < b[0]:
            k -= 1
    print(k)