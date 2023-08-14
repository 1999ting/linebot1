import requests
from bs4 import BeautifulSoup

def get_news():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    news_items = soup.select('.news_content .table .tr')
    latest_news1 = []

    for item in news_items[1:6]:
        news_date0 = item.find(class_='date').text
        news_title0 = item.select('.td:nth-child(2) title')[:5].text
        news_link0 = url + item.select('.td:nth-child(2) a')[:5]['href']
        
        news_info0 = f"日期：{news_date0}\n標題：{news_title0}\n連結：{news_link0}\n"
        latest_news1.append(news_info0)
    
    return '\n\n'.join(latest_news1)