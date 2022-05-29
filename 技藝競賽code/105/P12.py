for T in range(int(input())):
    value = input().strip().split()
    value_str = ''
    for i in range(len(value)):
        if value[i][0] == '.':
            cont = 0
            for j in range(len(value[i])):
                if value[i][j] == '.':
                    cont += 1
        elif value[i][0] == '-':
            if value[i].count('-') == len(value[i]):
                value_str += '0'
                continue
            cont = 5
            for j in range(len(value[i])):
                if value[i][j] == '-':
                    cont += 1
        value_str += str(cont)
    print(value_str)
