import requests
from bs4 import BeautifulSoup

def get_top5_data():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    data_elements = soup.find_all('div', class_='title')  # 假設標題在<div>標籤中，並有class為"title"
    for i in range(min(5, len(data_elements))):
        date_element = data_elements[i].find_previous('div', class_='date')  # 找到前一個相鄰的<div>標籤，並有class為"date"
        date = date_element.text.strip()
        title_element = data_elements[i].find('a')  # 找到<a>標籤
        title = title_element.text
        link = title_element['href']  # 提取連結的href屬性值
        data_list.append((date, title, link))
    return data_list