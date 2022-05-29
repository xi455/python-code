for T in range(int(input())):
    a = int(input())
    aa = []
    for i in range(9,1,-1):
        while int(a) % i == 0:
            aa.append(str(i))
            a /= i
    if int(a) <= 1 and aa != []:
        print(''.join(aa)[::-1])
    else:
        print(-1)