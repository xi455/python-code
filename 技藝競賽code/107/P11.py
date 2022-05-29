ans_ans=[]
for T in range(int(input())):
    a=input().strip().split()
    ans=len(a)
    cont=0
    for i in a:
        for j in i:
            if j =='s' or j == 'S':
                cont+=1
                break
    ans_ans.append(str(ans)+','+str(cont))
for i in ans_ans:
    print(i)