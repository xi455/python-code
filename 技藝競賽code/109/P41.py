import sys
for input in sys.stdin.read().splitlines():
    value = [int(i) for i in input.strip().split()]
 
    value_arr = [[0 for i in range(value[0]+1)]for j in range(value[1]+1)]
 
    val = value[2:]
 
    for i in range(1,len(value_arr)):
        for j in range(1,len(value_arr[0])):
            if val[i-1] > j:
                value_arr[i][j] = value_arr[i-1][j]
            else:
                value_arr[i][j] = max(value_arr[i-1][j] , value_arr[i-1][j-val[i-1]] + val[i-1])
    print(value_arr[-1][-1])