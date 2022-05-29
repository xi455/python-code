ans = []
for i in range(int(input())):
    a = input().strip().split()
    a_int = []
    for i in a:
        if i.isdigit() == True:
            a_int.append(i)
        else:
            # print('{}{}{}'.format(a_int[-1],i,a_int[-2]))
            aa = eval('{}{}{}'.format(a_int[-2], i, a_int[-1]))
            a_int.pop(), a_int.pop()
            a_int.append(int(aa))
    ans.append(str(a_int).replace('[', '').replace(']', ''))
for i in ans:
    print(i)
