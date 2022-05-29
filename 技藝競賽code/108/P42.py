for T in range(int(input())):
    a1 = int(input())
    a2 = int(input())
    a = [[i for i in list(map(int,input().strip().split()))] for j in range(a1)]
    a.insert(0,[999] * a2)
    for i in range(len(a)):
        a[i].insert(0,999)
    for i in range(1,a1 + 1):
        for j in range(1,a2 + 1):
            if i == 1 and j == 1: continue
            a[i][j] += min(a[i-1][j],a[i][j-1])
    print(a[a1][a2])