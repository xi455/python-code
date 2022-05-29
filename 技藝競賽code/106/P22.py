from itertools import permutations
ans=[]
for T in range(int(input())):
    a=input().strip().split(',')
    aa=(list(permutations(a[0])))
    a1,a2=int(a[1]),int(a[2])
    A,B=0,0
    for i in range(len(aa[0])):
        if aa[a1-1][i] == aa[a2-1][i]:
            A+=1
        elif aa[1][i] in aa[0]:
            B+=1
    ans.append('{}A{}B'.format(A,B))
for i in ans:
    print(i)
