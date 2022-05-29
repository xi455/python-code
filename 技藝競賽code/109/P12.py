for T in range(int(input())):
    a = [i for i in input().strip()]
    # print(a)
    a1 = a2 = ''
    for i in a:
        if i == '4':
            a1 += '3'
            a2 += '1'
        else:
            a1 += i
            a2 += '0'
    print(int(a1),int(a2))