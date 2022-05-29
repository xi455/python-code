for T in range(int(input())):
    bool = True
    big = smll = 0
    for i in input():
        if i == '[':
            big += 1
        elif i == '(':
            smll += 1
        elif i == ']':
            big -= 1
            if big < 0:
                # print('Try again')
                bool = False
                break
        elif i == ')':
            smll -= 1
            if smll < 0:
                # print('Try again')
                bool = False
                break
    if big != 0:
        bool = False
    elif smll != 0:
        bool = False
    
    if bool:
        print('Valid')
    else:
        print('Try again')