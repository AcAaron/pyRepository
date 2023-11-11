import requests
from bs4 import BeautifulSoup

urls=[
    f'https://books.toscrape.com/catalogue/page-{i+1}.html'
    for i in range(5)
]
li=[]
def put_li(t):
    li.append(t)
def craw(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    lines=soup.findAll('h3')
    for i in lines:
        put_li(i.string)
    return [line.string for line in lines]
if __name__=='__main__':
    for i in craw(urls[0]):
        print(i)
