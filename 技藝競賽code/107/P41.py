def printvalue(n,cont):
    if n < k:
        if a[n] and a[n] != 'null':
            cont += 1
            printvalue(n * 2,cont)
            aa.append(cont)
            printvalue(n * 2 + 1,cont)
 
        elif a[n] == 'null':
            if n * 2 < k or n * 2 + 1 < k:
                aa.append(0)
 
for T in range(int(input())):
    a = input().strip().replace('[','').replace(']','').split(',')
    a.insert(0,'0')
    n = 1
    aa = []
    cont = 0
    k = len(a)
    printvalue(n,cont)
    a1 = aa[:aa.index(1)]
    a2 = aa[aa.index(1)+1:]
 
    if a1 == []:
        print(max(a2)-1)
 
    elif a1 == [0]:
        print(max(a2))
 
    elif a2 == []:
        print(max(a1)-1)
 
    elif a2 == [0]:
        print(max(a1))
       
    else:
        print(max(a1)-1+max(a2)-1)
