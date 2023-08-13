from flask import Flask, request, abort
import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Line Bot 的 Channel Access Token 和 Channel Secret
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
handler = WebhookHandler('YOUR_CHANNEL_SECRET')

# 處理 Line Bot 的 Webhook 請求
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 爬取前五筆資料，包括日期、標題和連結
def get_top5_data():
    url = 'https://example.com'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    data_elements = soup.find_all('div', class_='title')  # 假設標題在<div>標籤中，並有class為"title"
    data_elements = soup.find_all('a', class_='link')
    for i in range(min(5, len(data_elements))):
        date_element = data_elements[i].find_previous('div', class_='date')  # 找到前一個相鄰的<div>標籤，並有class為"date"
        date = date_element.text.strip()
        title_element = data_elements[i].find('a')  # 找到<a>標籤
        title = title_element.text
        link = title_element['href']  # 提取連結的href屬性值
        data_list.append((date, title, link))
    return data_list

# Line Bot 的訊息處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    if user_message == '前五筆':
        top5_data = get_top5_data()
        reply_message = "前五筆資料：\n"
        for date, title, link in top5_data:
            reply_message += f"{date}\n- {title}\n  {link}\n"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )

if __name__ == "__main__":
    app.run()