def fib():
    i = 0
    j = 1
    while len(str(i)) < 18:
        i,j = j ,i + j
        val_list.append(i)
 
val_list = []
fib()
 
val_list = val_list[::-1]
val_list.pop()
for T in range(int(input())):
    val = int(input())
    val_num = val
    val_str = ''
 
    for i in range(len(val_list)):
        if val >= val_list[i]:
            val -= val_list[i]
            val_str += '1'
        else:
            val_str += '0'
    print(f'{val_num}={int(val_str)}')
