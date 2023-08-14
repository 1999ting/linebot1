from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

line_bot_api = LineBotApi('92kcy07IM75HrTqA3x+nCn61QmpKr0I5c1gH3Dumn5MR8DP1876/38wqBFlF/1KqP+R+cjzpqvxLD1NELcik69B92V8+k4Wt0ZroHxEoL5HZ19/nT7RC6v3j08G6AFd2/sFxfJy2tsy84WGEbNNrwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8cfd13f4a443434527574c3c6b80b0ab')

def crawl_website():
    url = 'https://www.ptt.cc/bbs/biker/index.html'  # 要爬取的網站的URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []

    for article in soup.find_all('r-ent'):  # 假設每篇文章都被<article>標籤包裹
        title = article.find('title').text
        link = article.find('a')['href']
        date = article.find('date').text
        articles.append({'title': title, 'link': link, 'date': date})

    return articles

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'ptt':
        articles = crawl_website()
        for article in articles:
            response += f"標題：{article['title']}\n連結：{article['link']}\n日期：{article['date']}\n\n"
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response)
        )

if __name__ == "__main__":
    app.run()