for T in range(int(input())):
    a = list(map(int, input().strip().split(',')))
    value = list(a)
    bb = []
    cont = 0
    k = len(a)
    while cont < k-1:
        a.sort()
        aa = []
        aa.append(a[0])
        aa.append(a[1])
        aa.append(a[1] + a[0])
        a[1] = a[0] + a[1]
        bb.append(aa)
        a.pop(0)
        cont += 1

    bb = bb[::-1]
    an = []
    for i in range(len(value)):
        num = 0
        bool = True
        while bool:
            for j in range(len(bb)):
                if value[i] in bb[j]:
                    if bb[j][-1] != bb[0][-1]:
                        num += 1
                        value[i] = bb[j][-1]
                        break
                    else:
                        num += 1
                        bool = False
                        break
        value[i] = num
    value = list(map(str, value))
    print(','.join(value))
