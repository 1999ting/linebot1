import requests
from bs4 import BeautifulSoup
# 油價查詢
def bikerptt():
    target_url1 = 'https://www.ptt.cc/bbs/biker/index.html'
    rs = requests.session()
    res = rs.get(target_url1, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    date = soup.select('#date')[:5].text.replace('\n', '')
    title = soup.select('#title')[:5].text.replace('\n\n\n', '').replace(' ', '')
    href = soup.select('#href')[:5].text.replace(' ', '')
    content = '{}\n{}{}'.format(date, title, href)
    return content