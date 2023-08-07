from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('92kcy07IM75HrTqA3x+nCn61QmpKr0I5c1gH3Dumn5MR8DP1876/38wqBFlF/1KqP+R+cjzpqvxLD1NELcik69B92V8+k4Wt0ZroHxEoL5HZ19/nT7RC6v3j08G6AFd2/sFxfJy2tsy84WGEbNNrwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8cfd13f4a443434527574c3c6b80b0ab')

# 監聽
@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']


    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)


    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
    
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    emoji = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435"
                "emojiId": "011"
            },
            {
                "index": 17,
                "productId": "5ac1bfd5040ab15980c9b435",
                "emojiId": "020"
            }
    ]
    text_message = TextSendMessage(text='''$ Master Finance $
Hello! 您好 歡迎您加入此群組 
                                   
我是財經小幫手 很高興為您服務 
                                   
歡迎您詢問個是財經問題
也可點及下列連結觀看個是財經線上資訊
歡迎各位一起討論''', emojis=emoji)

    sticker_message = StickerSendMessage(
        package_id ='11538',
        sticker_id='51626530'
    )
    line_bot_api.reply_message(
        event.reply_token, 
        [text_message, sticker_message])

if __name__ == "__main__":
    app.run()