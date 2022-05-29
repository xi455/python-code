import requests
import bs4
import os

def datagat(url):
    my_headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    req=requests.get(url,headers=my_headers)

    root=bs4.BeautifulSoup(req.text,'lxml')

    src=root.find_all('a',{'class':'showcase__link'})

    img=[i.img.get('data-src')for i in src]
    id=[str(i.img.get('alt')).replace('\n','').replace('/','').replace('\r','') for i in src]

    for i in range(len(img)):

        if not os.path.exists('images'):
            os.mkdir('images')

        image=requests.get(img[i])

        with open('images\\' + id[i] + '.jpg','wb')as file:
           file.write(image.content)

    return ('https://www.freepik.com/search?dates=any&format=search&page={}&query={}'.format(number+1,name))

name=input('查詢:')
page=int(input('幾頁:'))
url=(f'https://www.freepik.com/search?format=search&page=1&query={name}')
number=1
while True:
    url=datagat(url)
    number+=1
    print(number)