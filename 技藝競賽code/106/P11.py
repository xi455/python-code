for T in range(int(input())):
    a = [i for i in input().strip().split() if 's' in i or 'S' in i]
    print(len(a))
