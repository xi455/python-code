for T in range(int(input())):
    a = list(map(int,input().strip().split()))
    a.sort()
    print(a[-1],a[-2])