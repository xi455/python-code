for T in range(int(input())):
    val = [int(i) for i in input().strip().split()]
 
    left = ''
    right = []
    val_list = []
 
    left += str(val[0] // val[1]) + '.'
    num = val[0] % val[1]
 
    while num != 0 and len(right) < 50 and num not in val_list:
        val_list.append(num)
        num *= 10
        right.append(str(num // val[1]))
        num %= val[1]
 
    if num in val_list:
        right.insert(val_list.index(num),'(')
        right.append(')')
        print(left + ''.join(right))
 
    elif len(right) >= 50:
        right.insert(0,'(')
        right.append('...)')
        print(left + ''.join(right))
 
    elif num == 0:
        print(left + ''.join(right) + '(0)')