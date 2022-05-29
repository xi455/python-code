import urllib.request as req #網路資源(URLs)擷取套件
url='https://www.ptt.cc/bbs/movie/index.html' #要爬取的網址

request=req.Request(url,headers={ #模擬一般線上用戶訪問的樣子
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
})

with req.urlopen(request)as response: #將得到的網站內容request代入response並且讀取打開放到了data
    data=response.read().decode("utf-8")

import bs4 #HTML剖析套件，功能簡單說就是去除網站上的髒東西(亂碼)
root=bs4.BeautifulSoup(data,"html.parser")  #讓它辨識html並且只把html的東西挑出放入root
titles=root.find_all("div",class_="title")  #在root裡的html找尋class="title"的div標籤放入titles

for title in titles: #跑titles進title迴圈，如果遇到那種被廢棄沒有<a>(html語法)的title不予顯示
    if title.a != None:
        print(title.a.string)

# 用爬蟲得到這網站的標題內容