#載入LineBot所需要的套件
from line_bot_api import *
from events.basic import *
from events.oil import *
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('92kcy07IM75HrTqA3x+nCn61QmpKr0I5c1gH3Dumn5MR8DP1876/38wqBFlF/1KqP+R+cjzpqvxLD1NELcik69B92V8+k4Wt0ZroHxEoL5HZ19/nT7RC6v3j08G6AFd2/sFxfJy2tsy84WGEbNNrwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8cfd13f4a443434527574c3c6b80b0ab')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
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
    message_text = str(event.message.text).lower()

    ############################## 使用說明 選單 油價查詢####################################
    if message_text == '@使用說明':
        about_us_event(event)
        Usage(event)
        oil_price(event)

    if event.message.text == "想知道油價":
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))


    # if event.message.text == "@小幫手":
    #     buttons_template = TemplateSendMessage(
    #         alt_text='小幫手 template',
    #         template=ButtonsTemplate(
    #             title='選擇服務',
    #             text='請選擇',
    #             thumbnail_image_url='https:/i.imgur.com/2WUTjOE.jpg',
    #             actions=[
    #                 MessageTemplateAction(
    #                     label='油價查詢',
    #                     text='油價查詢'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='匯率查詢',
    #                     text='匯率查詢'
    #                 ),
    #                 MessageTemplateAction(
    #                     label='股價查詢',
    #                     text='股價查詢'
    #                 )
    #             ]
    #         )
    #     )
    #     line_bot_api.reply_message(event.reply_token, buttons_template)

if __name__ == "__main__":
    app.run()