import sys
for input in sys.stdin.read().splitlines():
    a = [i for i in input]
    long = False
    big = False
    smll = False
    bigsmll = False
    aa = False
    aa_num = False
    aa_alpha = False
    aa_num_alpha = False
    num = False
    if len(a) >= 8:
        long = True
    
    for i in a:
        if i.isupper() == True:
            big = True
            break
    
    for i in a:
        if i.islower() == True:
            smll = True
            break

    if big == True and smll == True:
        bigsmll = True

    for i in a:
        if i.isalpha() == False and i.isdigit() == False:
            aa = True
            
        if i.isdigit() == True:
            aa_num = True
        
        if i.isalpha() == True:
            aa_alpha = True
    if aa_num == True and aa_alpha == True:
        aa_num_alpha = True
    elif aa == True  and aa_alpha == True:
        aa_num_alpha = True

    # for i in a:
    #     if i.isdigit() == True:
    #         num = True
    #         break

    b = []
    b.append(long)
    b.append(bigsmll)
    b.append(aa_num_alpha)
    # b.append(num)

    # print(b)

    if b.count(True) == 3:
        print('This password is STRONG')
    elif b.count(True) == 2:
        print('This password is GOOD')
    elif b.count(True) == 1:
        print('This password is ACCEPTABLE')
    elif b.count(True) == 0:
        print('This password is WEAK')