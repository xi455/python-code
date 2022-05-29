for T in range(int(input())):
    a1,a2 = list(map(int,input().strip().split()))
    b = [[i for i in input().strip()] for j in range(a1)]
    c = [[b[i][j] for i in range(a1)] for j in range(a2)]
    c1 = ['A','C','G','T']
    aa = []
    for i in c:
        c2 = [0,0,0,0]
        for j in range(len(i)):
            if i[j] in c1:
                c2[c1.index(i[j])] += 1
        if c2.count(c2[0]) == 4:
            aa.append('A')
        else:
            aa.append(c1[c2.index(max(c2))])
    print(''.join(aa))