val = int(input())
k = val
val_any = []
val_list = []
 
for j in range(val,0,-1):
    for i in range(val,0,-1):
        if val == 0:
            break
        elif i > j:
            continue
        if val >= i:
            while val != 0 and val >= i:
                val -= i
                val_list.append(str(i))
   
    val_any.append(val_list)
    val_list = []
    val = k
 
for i in range(len(val_any)):
    if len(val_any[i]) == 1:
        continue
    val_any[i] = val_any[i][::-1]
    val_li = []
    for j in range(len(val_any[i])-1):
        if val_any[i][j] != '1':
            val_li.append('1' * int(val_any[i][j]))
        else:
            val_li.append(val_any[i][j])
    val_li.append(val_any[i][j+1])
    if val_li != [] and val_li not in val_any:
        val_any.append(val_li[::-1])
        val_any[i] = val_any[i][::-1]
    else:
        val_any[i] = val_any[i][::-1]
        val_li = []
 
val_any.sort(reverse=True)
# print(val_any)
 
for i in range(len(val_any)):
    print(''.join(val_any[i]))
