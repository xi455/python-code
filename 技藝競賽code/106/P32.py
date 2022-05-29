for T in range(int(input())):
    value = input().strip().split(', ')
    value_any = []
 
    for i in range(len(value)):
        value_num = 0
        values = []
        for j in range(len(value[i])):
            value_num += int(value[i][j])
        values.append(len(value[i]))
        values.append(value_num)
        value_any.append(values)
 
    value_any_2 = list(value_any)
    value_any_2.sort()
   
    for i in range(len(value_any_2)):
        value_any[i] =str(value_any_2.index(value_any[i]) + 1)
    print(', '.join(value_any))
