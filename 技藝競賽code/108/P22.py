for T in range(int(input())):
    a = list(map(int,input().strip().split()))
    print(a[0] ** a[1] % a[2])