moon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# moon_1 = [0,31,29,31,30,31,30,31,31,30,31,30,31]
 
val = [int(i) for i in input().strip().split('/')]
# print(val)
 
bool = True
if val[0] % 4 == 0 and val[0] % 100 != 0:
    bool = True #閏年
elif val[0] % 400 == 0:
    bool = True
else:
    bool = False #平年
 
if bool == True:
    sky = sum(moon[:val[1]]) + val[2] + 1
    if sky % 7 != 0:
        week = sky // 7 + 1
    else:
        week = sky // 7
    day = moon[val[1]]
 
    monday = (val[0] + (val[0]//4) + (val[0]//400) - (val[0]//100) + (val[1]+val[2])-1) % 7
else:
    sky = sum(moon[:val[1]]) + val[2]
    # print(sky)
    if sky % 7 != 0:
        week = sky // 7 + 1
    else:
        week = sky // 7
 
    day = moon[val[1]]
 
    monday = (val[0] + (val[0]//4) + (val[0]//400) - (val[0]//100) + (val[1]+val[2])-1) % 7
    # print(val[0] + (val[0]//4) + (val[0]//400) - (val[0]//100) + (val[1]+val[2])-1)
# print(monday % 7)
print(f'{sky}天')
print(f'{week}週')
print(f'{day}天')
# print(monday)
 
if monday == 1:
    print('星期日')
elif monday == 2:
    print('星期一')
elif monday == 3:
    print('星期二')
elif monday == 4:
    print('星期三')
elif monday == 5:
    print('星期四')
elif monday == 6:
    print('星期五')
elif monday == 0:
    print('星期六')
