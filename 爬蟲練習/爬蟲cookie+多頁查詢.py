import urllib.request as req
with open('a.txt','w',encoding="utf-8")as data:
    data.write("")
def getdata(url):
    request=req.Request(url,headers={ #有些網站會有些阻擋的cookie，所以要找到那個cookie模擬進來
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"})
    with req.urlopen(request)as response:
        data=response.read().decode("utf-8")

    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")  #辨識html
    titles=root.find_all("div",class_="title")  #找尋class="title"的div標籤

    with open('a.txt','a',encoding="utf-8")as data:
        for title in titles:
            if title.a != None:
                print(title.a.string)
                data.write(title.a.string+"\n")

    nextlink=root.find("a",string="‹ 上頁") #抓上一頁的html語法放入nextlink
    return nextlink["href"] #分類抓出html上頁裡的href網址名稱放入nextlink回傳
pageurl='https://www.ptt.cc/bbs/movie/index.html'
count=0
while count<5: #代表要抓5頁的資料
    pageurl="https://www.ptt.cc"+getdata(pageurl) #nextlink雖然會回傳href網址，但前面的https://www.ptt.cc要在另加上去
    count+=1