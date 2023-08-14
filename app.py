from flask import Flask, request, abort
import requests
from bs4 import BeautifulSoup
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('92kcy07IM75HrTqA3x+nCn61QmpKr0I5c1gH3Dumn5MR8DP1876/38wqBFlF/1KqP+R+cjzpqvxLD1NELcik69B92V8+k4Wt0ZroHxEoL5HZ19/nT7RC6v3j08G6AFd2/sFxfJy2tsy84WGEbNNrwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8cfd13f4a443434527574c3c6b80b0ab')

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

# 爬取最新的5筆資料
def get_latest_data():
    url = 'https://www.ptt.cc/bbs/biker/index.html'
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    data_list = []
    # 假設資料是在<div class="data">...</div>標籤中
    data_elements = soup.find_all('div', class_='data')
    for data_element in data_elements[:5]:
        data_list.append(data_element.text)
    return data_list

# Line Bot 的訊息處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    if user_message == 'ptt':
        latest_data = get_latest_data()
        reply_message = "最新的5筆資料：\n"
        for data in latest_data:
            reply_message += f"- {data}\n"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_message)
        )

if __name__ == "__main__":
    app.run()