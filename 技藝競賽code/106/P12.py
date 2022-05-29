english = ['M','D','C','L','X','V','I']
number = [1000,500,100,50,10,5,1]
 
for T in range(int(input())):
    val = [i for i in input().strip()]
    # print(val)
 
    cont = number[english.index(val[0])]
    for i in range(1,len(val)):
        a = number[english.index(val[i])]
        b = number[english.index(val[i-1])]
        if a <= b:
            cont += a
        else:
            cont -= b
            cont += a - b
    print(cont)
