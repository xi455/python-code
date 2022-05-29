import math
for T in range(int(input())):
    value = [int(i) for i in input().strip().split(',')]
    max = 0
    for i in range(len(value)):
        for j in range(len(value)):
            if value[i] == value[j]:
                continue
            if math.gcd(value[i],value[j]) > max:
                max = math.gcd(value[i],value[j])
    print(max)
