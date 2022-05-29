import sys
a = []
aa = []
for input in sys.stdin.read().splitlines():
    a.append(input.strip().split())
    for i in input.strip().split():
        aa.append(i)
# print(a)

an = []
a_one = []
for i in a:
    if i[::-1] not in a:
        an.append(i[::-1])

for i in aa:
    if i not in a_one:
        a_one.append(i)

if an != []:
    # print(an)
    for i in an:
        print(' '.join(i))
else:
    # print(a_one)
    # print([a_one[0]] * 2)
    for i in range(len(a_one)):
        an = [a_one[i]] * 2
        if an not in a:
            print(' '.join(an))
            break
