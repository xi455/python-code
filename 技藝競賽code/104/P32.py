def value(i,j):
    cont = 0
    cont_an = 0
    for k in range(c):
        if A[i][k] == 9999:
            cont_an = B[k][j]
        elif B[k][j] == 9999:
            cont_an = A[i][k]
        else:
            cont += A[i][k] * B[k][j]
    if cont_an != 0:
        cont = C[i][j] - cont
        cont /= cont_an
    num_list.append(int(cont))
 
for T in range(int(input())):
    a,b,c,d = list(map(int,input().strip().split(',')))
    A = [[i for i in list(map(int,input().split()))]for j in range(a)]
    B = [[i for i in list(map(int,input().split()))]for j in range(c)]
    C = [[i for i in list(map(int,input().split()))]for j in range(a)]
    num_list = []
    for i in range(a):
        for j in range(d):
            for k in range(c):
                if 9999 in A[i] or B[k][j] == 9999:
                    value(i,j)
                    break
 
    if num_list.count(num_list[0]) == len(num_list):
        print(num_list[0])
        continue
    for i in range(len(num_list)):
        if num_list.count(num_list[i]) > (b//2):
            print(num_list[i])
            break
