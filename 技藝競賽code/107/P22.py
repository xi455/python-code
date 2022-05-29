ans=[]
for T in range(int(input())):
    a=input().strip().split(',')
    aa=a[1:-1]
    bb=''
    b=[]
    N=int(a[0])
 
    def ab(bb):
        if len(bb)==N:
            b.append(bb)
        for i in range(len(aa)):
            if aa[i] not in bb:
                ab(bb+str(aa[i]))
                
    ab(bb)
    ans.append(b[int(a[-1])-1])
for i in ans:
    print(i)
