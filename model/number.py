import requests
from bs4 import BeautifulSoup

def get_latest_news1():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')

    news_items = soup.select('.news_content .table .tr')
    latest_news = []

    for item in news_items:
        news_date = item.find(class_='date').text
        news_title = item.select(class_='title')[:5].text
        news_link = url + item.select('a')[:5]['href']
        
        news_info = f"日期：{news_date}\n標題：{news_title}\n連結：{news_link}\n"
        latest_news.append(news_info)
    
    return '\n\n'.join(latest_news)