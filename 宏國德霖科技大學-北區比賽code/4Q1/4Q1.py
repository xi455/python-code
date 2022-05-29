value = [int(i) for i in input().strip().split(',')]
# print(value)
value = value[::-1]
# print(value)

s = 1
k = 1

for i in range(1,len(value)):
    s = value[0]
    k = (s * value[i]) + k
    value[0],k = k,s
    # print(value)
    # s = value[0]
    # k = s
print(k,value[0],sep='\n')