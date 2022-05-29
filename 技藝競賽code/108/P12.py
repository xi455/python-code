for T in range(int(input())):
    a = input().strip().split()
    any = 0
    num = 0
    cont = 0
    for i in range(len(a)):
        if any < 10:
            if a[i] == '/':
                num += 1
                cont -= int(a[i-1])
                cont += 10
                if a[i+1] == 'X':
                    cont += 10
                else:
                    cont += int(a[i+1])
            elif a[i] == 'X':
                cont += 10
                if a[i+1] == 'X':
                    cont += 10
                    if a[i+2] == 'X':
                        cont += 10
                    else:
                        cont += int(a[i+2])
                elif a[i+2] == '/':
                    cont += 10
                else:
                    cont += int(a[i+1])
                    cont +=int(a[i+2])
            else:
                cont += int(a[i])
                num += 1
        else:
            break
        if num == 2:
            num = 0
            any += 1
        elif a[i] == 'X':
            any += 1
    print(cont)
