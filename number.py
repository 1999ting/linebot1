import requests
from bs4 import BeautifulSoup

def get_latest_data():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    # 假設資料是在<div class="data">...</div>標籤中
    data_elements = soup.find_all('div', class_='title')
    for data_element in data_elements[:5]:
        data_list.append(data_element.text)
    return data_list