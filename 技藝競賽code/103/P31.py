def kk():
    cont = 1
    val_arr = [[i for i in range(1,14)]for j in range(5)]
    # val_arr = []
    for i in range(1,5):
        for j in range(13):
            val_arr[i][j] = cont
            cont += 1
    # print(val_arr)
    return val_arr
val_arr = kk()
 
def kk_7():
    cont = 1
    for i in range(1,len(val)):
        if val[i] - val[i-1] == 1:
            cont += 1
    if cont == 5:
        print(7)
        return False
    else:
        return True
       
for T in range(int(input())):
    val = [int(i) for i in input().strip().split()]
    val.sort()
    val_num = []
 
    for i in val:
        for j in range(len(val_arr)):
            if i in val_arr[j]:
                val_num.append(val_arr[0][val_arr[j].index(i)])
                break
 
    val_num.sort()
    boo = kk_7()
 
    if boo:
        cont = 1
        for i in range(1,len(val_num)):
            if val_num[i] - val_num[i-1] == 1:
                cont += 1
 
        if cont == 5:
            print(4)
            boo = False
 
    if boo:
        if 1 in val_num and 10 in val_num and 11 in val_num and 12 in val_num and 13 in val_num:
            for i in range(len(val_num)):
                if val_num[i] == 1:
                    if val_num[-1] - val_num[i] < 13:
                        print(7)
                        boo = False
                        break
            if boo:
                print(4)
                boo = False
   
    if boo:
        for i in val_num:
            if val_num.count(i) >= 4:
                print(6)
                boo = False
                break
 
    if boo:
        for i in val_num:
            if val_num.count(i) >= 3:
                for j in val_num:  
                    if j == i:
                        continue
 
                    if val_num.count(j) >= 2:
                        print(5)
                        boo = False
                        break
 
                if boo:
                    print(3)
                    boo = False
                    break
                else:
                    break
 
    if boo:
        for i in val_num:
            if val_num.count(i) >= 2:
                for j in val_num:
                    if i == j:
                        continue
 
                    if val_num.count(j) >= 2:
                        print(2)
                        boo = False
                        break
 
                if boo:
                    print(1)
                    boo = False
                    break
                else:
                    break
 
    if boo:
        print(0)
