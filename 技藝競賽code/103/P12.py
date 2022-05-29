for T in range(int(input())):
    val = [int(i) for i in input().strip().split(',')]
    val_an = val[-1] - val[0] * val[1]
    val_y = val[2] - val[1]
    Y = val_an // val_y
    X = (val[-1] - Y * val[2]) // val[1]
    print('{},{}'.format(X,Y))
