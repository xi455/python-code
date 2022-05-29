for T in range(int(input())):
    values = input().strip().split('/')
 
    value_left = [int(i) for i in values[0].split('.')]
    value_right = [int(i) for i in values[1].split('.')]
 
    for i in range(len(value_left)):
        value_left[i] = '{:b}'.format(value_left[i])
 
    for i in range(len(value_right)):
        value_right[i] = '{:b}'.format(value_right[i])
 
    for i in range(len(value_left)):
        if len(value_left[i]) != 8:
            value_left[i] = ('0' * (8 - len(value_left[i]))) + value_left[i]
   
    for i in range(len(value_right)):
        if len(value_right[i]) != 8:
            value_right[i] = ('0' * (8 - len(value_right[
i]))) + value_right[i]
 
    for i in range(len(value_right)):
        value_str = ''
        for j in range(len(value_right[i])):
            if value_right[i][j] == '1':
                value_str += '0'
            else:
                value_str += '1'
        value_right[i] = value_str
 
    for i in range(len(value_left)):
        value_str = ''
        for j in range(len(value_left[i])):
            if value_left[i][j] == '1' or value_right[i][j] == '1':
                value_str += '1'
            else:
                value_str += '0'
        value_right[i] = value_str
 
    for i in range(len(value_right)):
        value_right[i] = str(int(value_right[i],2))
 
    print('.'.join(value_right))
