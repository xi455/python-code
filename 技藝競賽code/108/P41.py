for T in range(int(input())):
    a1 = int(input())
    a2 = int(input())
    a_list = [None] * a1
    b = []
    for i in range(a2):
        a = list(map(int, input().strip().split()))
        a_list[a[0]] = True
        a_list[a[1]] = False
        b.append(a)
    for i in range(a2):
        if a_list[b[i][0]] == True:
            a_list[b[i][1]] = False
        elif a_list[b[i][0]] == False:
            a_list[b[i][1]] = True
    bool = True
    for i in range(len(b)):
        if a_list[b[i][0]] == a_list[b[i][1]]:
            bool = False
            break
    print('T') if bool else print('F')
