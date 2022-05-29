val = int(input())
val_list = []
cont = 0
for i in range(val+1):
    for j in str(i):
        if j == '1':
            cont += 1
            val_list.append(str(i))
print(cont)
for i in range(len(val_list)):
    print(''.join(val_list[i]))
# print(val_list)
