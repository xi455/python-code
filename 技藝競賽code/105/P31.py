def max_tree_fn():
    for i in range(1,len(val)):
        if i * 2 < len(val):
            if val[i * 2] < val[i]:
                return False
        if i * 2 + 1 < len(val):
            if val[i * 2 + 1] < val[i]:
                return False
    return True
 
def min_tree_fn():
    for i in range(1,len(val)):
        if i * 2 < len(val):
            if val[i * 2] > val[i]:
                return False
        if i * 2 + 1 < len(val):
            if val[i * 2 + 1] > val[i]:
                return False
    return True
 
def Bin_tree_fn():
    for i in range(1,len(val)):
        if i * 2 < len(val):
            if val[i * 2] > val[i]:
                return False
        if i * 2 + 1 < len(val):
            if val[i * 2 + 1] < val[i]:
                return False
    return True
 
for T in range(int(input())):
    val = [int(i) for i in input().strip().split(',')]
 
    val.insert(0,None)
 
    min = min_tree_fn()
    max = max_tree_fn()
    Bin = Bin_tree_fn()
 
    if min == True or max == True:
        print('H')
    elif Bin == True:
        print('B')
    else:
        print('F')
