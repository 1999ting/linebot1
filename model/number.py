import requests
from bs4 import BeautifulSoup

def get_top5_data():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    # 假設日期、標題和連結在<div class="data">...</div>標籤中
    data_elements = soup.find_all('div', class_='data')
    for i in range(min(5, len(data_elements))):
        date = data_elements[i].find('span', class_='date').text
        title = data_elements[i].find('title').text
        link = data_elements[i].find('a', class_='link')['href']
        data_list.append((date, title, link))
    return data_list
