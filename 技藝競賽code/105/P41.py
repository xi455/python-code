for T in range(int(input())):
    val_1 = [i for i in input().strip()]
    val_2 = [i for i in input().strip()]
    val_1.insert(0,'0')
    val_2.insert(0,'0')
 
    array = [[0 for i in range(len(val_2))] for j in range(len(val_1))]
   
    for i in range(1 ,len(val_1)):
        for j in range(1 ,len(val_2)):
            if val_1[i] == val_2[j]:
                array[i][j] = array[i - 1][j - 1] + 1
            else:
                array[i][j] = max(array[i][j-1] ,array[i-1][j])
 
    print(array[-1][-1])
