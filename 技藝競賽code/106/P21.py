for T in range(int(input())):
    a = [int(i) for i in input().strip()]
    for i in range(len(a)):
        if i % 2 == 0:
            a[i] *= 2
    for i in range(len(a)):
        if a[i] >= 10:
            a[i] -= 9
    a_sum = sum(a)
    if a_sum % 10 == 0:
        print('T')
    else:
        print('F')
