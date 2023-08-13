import requests
from bs4 import BeautifulSoup

def get_top5_data():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    # 假設日期、標題和連結在<div class="data">...</div>標籤中
    data_elements = soup.find_all('div', class_='title')
    data_elements = soup.find_all('a', class_='link')
    data_elements = soup.find_all('div', class_='date')

    for i in range(min(5, len(data_elements))):
        date = data_elements[i].text.strip()
        title = data_elements[i].text.split('] ')[1]
        link = data_elements[i]['href']
        data_list.append((date, title, link))
    return data_list
