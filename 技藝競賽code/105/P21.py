for T in range(int(input())):
    value = input().strip().split('/')
 
    value_left = [int(i) for i in value[0].split('.')]
    value_right = [int(i) for i in value[1].split('.')]
 
    for i in range(len(value_left)):
        value_right[i] = str(bin(value_left[i] & value_right[i])[2:])
 
    for i in range(len(value_right)):
        value_right[i] = str(int(value_right[i],2))
    print('.'.join(value_right))
