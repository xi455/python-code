ans=[]
for T in range(int(input())):
    a=input().strip()
    b=a[::-1]
    while str(a) != b:
        a=int(a)+int(b)
        b=str(a)[::-1]
    ans.append(a)
for i in ans:
    print(i)