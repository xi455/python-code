ans=[]
for j in range(int(input())):
    a=input().strip().split()
    a=list(map(int,a))
    ab=0
    max=0
    for i in range(len(a)):
        ab+=a[i]
        if ab>max or max==0:
            max=ab
        if ab<=0:
            ab=0
    ans.append(max)
for i in ans:
    print(i)