ans=[]
for T in range(int(input())):
    a=input().strip().split()
    a=list(map(int,a))
 
    cont=0
    for s in range(a[4],a[5]+1):
        for i in range(a[0],a[1]+1):
            for j in range(a[2],a[3]+1):
                if (i+j)%s==(i-j)%s:
                    cont+=1
 
    ans.append(cont)
for i in ans:
    print(i)
