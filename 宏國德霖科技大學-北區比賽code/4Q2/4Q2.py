with open('in1.txt',mode='r',encoding='utf-8') as file:
    a = file.readline().strip().split()
    a = list(map(int,a))
    a.sort()
    a_list = []
    cont = 0
    for i in a:
        if i > 0:
            cont += i
            a_list.append(cont)

    # print(a_list)
    bb = str(sum(a_list)) + '='
    a_list = list(map(str,a_list))
    # print(a_list)
    aa = ('+'.join(a_list))
    print(bb + aa)
    # print(str(sum(a_list))+'='+('+').join(a_list))
    with open('out.txt',mode='w',encoding='utf-8')as fll:
        fll.writelines(bb + aa)