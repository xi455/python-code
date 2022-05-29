import tkinter as tk
 
moon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def main():
    # moon_1 = [0,31,29,31,30,31,30,31,31,30,31,30,31]
 
    # val = [int(i) for i in input().strip().split('/')]
    val =[int(i) for i in enty1.get().split('/')]
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
    entry = tk.Entry(width=20)
    lab = tk.Label(text=f'一年的第幾天:')
    # lab.pack()
    entry.insert(0,sky)
    lab.grid(row=2,column=0)
    entry.grid(row=2,column=1)
    # print(f'{sky}天')
 
    entry = tk.Entry(width=20)
    lab = tk.Label(text=f'一年的第幾週:')
    # lab.pack()
    entry.insert(0,week)
    lab.grid(row=3,column=0)
    entry.grid(row=3,column=1)
    # print(f'{week}週')
    entry = tk.Entry(width=20)
    lab = tk.Label(text=f'該月份有幾天:')
    # lab.pack()
    entry.insert(0,day)
    lab.grid(row=4,column=0)
    entry.grid(row=4,column=1)
    # print(f'{week}週')
 
    entry = tk.Entry(width=20)
    lab = tk.Label(text=f'該月份有幾天:')
    # lab.pack()
    # entry.insert(0,day)
    # entry.insert(0,week)
    lab.grid(row=4,column=0)
    entry.grid(row=4,column=1)
    # print(f'{day}天')
    # print(monday)
   
    if monday == 1:
        entry = tk.Entry(width=20)
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期天')
        # print('星期日')
    elif monday == 2:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期一')
        # print('星期一')
    elif monday == 3:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期二')
        # print('星期二')
    elif monday == 4:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期三')
        # print('星期三')
    elif monday == 5:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期四')
        # print('星期四')
    elif monday == 6:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期五')
        # print('星期五')
    elif monday == 0:
        lab = tk.Label(text='當天是星期幾: ')
        entry.insert(0,'星期六')
        # print('星期六')
    # lab.pack()
    lab.grid(row=5,column=0)
    entry.grid(row=5,column=1)
 
window = tk.Tk()
window.title('out')
window.geometry('300x200+750+100')
 
lab = tk.Label(text='日期:')
lab.grid(row=0,column=0)
 
enty1 = tk.Entry(width= 20)
# enty1.pack()
enty1.grid(row=0,column=1)
 
# enty2 = tk.Entry(width= 20)
# enty2.pack()
 
button = tk.Button(text='查詢',command= main)
# button.pack()
button.grid(row = 0,column=2)
 
window.mainloop()
