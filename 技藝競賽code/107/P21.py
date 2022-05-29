ans=[]
for T in range(int(input())):
    a=input().strip()
    b=int(a)
    a1=[]
    ab=b
    ac=[]
    while True:
        a1=[i for i in str(ab)]
        ab=0
        for i in range(len(a1)):
            ab+=int(a1[i])**2
 
        if ab==1:
            ans.append('T')
            break
        elif ab==b or ab==4:
            ans.append('F')
            break
for i in ans:
    print(i)
