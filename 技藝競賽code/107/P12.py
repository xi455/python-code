ans=[]
for T in range(int(input())):
    aa=input().strip()
    bb=input().strip()
    cc=input().strip()
    a=[a for a in aa]
    b=[b for b in bb]
    c=[c for c in cc]
    abc=''
    if a[0]==b[0] and a[0]==c[0]:
        if a[0]!='0':
            abc+=a[0]
            ans.append(a[0])
 
    if a[1]==b[1] and a[1]==c[1]:
        if a[1]!='0':
            abc+=a[1]
            ans.append(a[1])
 
    if a[2]==b[2] and a[2]==c[2]:
        if a[2]!='0':
            abc+=a[2]
            ans.append(a[2])
 
    if a.count(a[0])==3 and a[0]!='0':
        abc+=a[0]
        ans.append(a[0])
 
    if b.count(b[0])==3 and b[0]!='0':
        abc+=b[0]
        ans.append(b[0])
 
    if c.count(c[0])==3 and c[0]!='0':
        abc+=c[0]
        ans.append(c[0])
 
    if a[0]==b[1]and a[0]==c[2]:
        if a[0]!='0':
            abc+=a[0]
            ans.append(a[0])
 
    if a[2]==b[1]and a[2]==c[0]:
        if a[2]!='0':
            abc+=a[2]
            ans.append(a[2])
    if abc=='':
        ans.append(3)
for i in ans:
    print(i)
