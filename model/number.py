import requests
from bs4 import BeautifulSoup

def ptt_motor():
    target_url = 'https://www.ptt.cc/bbs/biker/index.html'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    date = soup.select('#date')[0].text.replace('\n', '')
    title = soup.select('#title')[0].text.replace('\n\n\n', '').replace(' ', '')
    link = soup.select('a','#link')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(date, title, link)
    return content
