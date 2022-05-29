ans=[]
for T in range(int(input())):
    a=input().strip().split(',')
    # a=['20', '8', '30']
    a=list(map(int,a))
    # print(a)
    aa=[]
    for i in a:
        ab=[]
        for j in range(1,i+1):
            if i % j ==0:
                ab.append(j)
        aa.append(ab)
    # print(aa)
    gcd=set()
    for i in aa[0]:
        for j in range(len(aa)):
            if j == 0: continue
            if i in aa[j]:
                gcd.add(i)
            else:
                if i in gcd:
                    gcd.remove(i)
    # print(gcd)
    gcd=list(map(int,gcd))
 
    for i in range(len(gcd)):
        for j in aa:
            if gcd[i] not in j and gcd[i] in gcd:
                gcd[i]=0
                break
 
    ans.append(max(gcd))
# print()
for i in ans:
    print(i)
