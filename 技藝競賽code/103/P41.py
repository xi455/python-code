num = ['00','01','100','101','1100','1101','11100','11101','111100','111101']
alpha = ['','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
'U','V','W','X','Y','Z','A','B','B']
 
for T in range(int(input())):
    val = input().strip()
    val_str = ''
    val_num_str = ''
    for i in range(len(val)):
        val_str += val[i]
        if val_str in num:
            val_num_str += str(num.index(val_str))
            val_str = ''
 
    print(alpha[int(val_num_str)])
