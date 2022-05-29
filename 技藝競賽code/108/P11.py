ans_ans=[]
for j in range(int(input())):
    a=input().strip()
    ab=0
    ans=0
    for i in a:
        if i=="O":
            ab+=1
        elif i =="X":
            ab=0
        ans+=ab
    ans_ans.append(ans)
for i in ans_ans:
    print(i)