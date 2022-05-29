value = [int(i) for i in input().strip().split()]
# print(value)

a_set = set()
cont = 2
num = 0
for i in range(2,value[1]+1):
    if i ** cont > value[1]:
        break
    while True:
        k = i ** cont
        if k >= value[0] and k <= value[1]:
            # num += 1
            a_set.add(k)
            # print(i ** cont)
        if k >value[1]:
            cont = 2
            break
        cont += 1
print(len(a_set))