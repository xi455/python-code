def val_fun(val_str):
    if len(val_str) >= val_len:
        val_list.append(int(val_str))
    for i in range(len(val[0])):
        if val[0][i] not in val_str:
            val_fun(val_str + val[0][i])
 
for T in range(int(input())):
    val = input().strip().split(',')
    val_str = ''
    val_len = len(val[0])
    val_list = []
   
    val_fun(val_str)
    print(val_list[int(val[1])-1] + val_list[int(val[2])-1])