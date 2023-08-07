from line_bot_api import *


def about_us_event(event):
    emoji = [
            {
                "index": 0,
                "productId": "5ac1bfd5040ab15980c9b435",
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
    
def push_msg(event,msg):
        try:
            user_id = event.source.user_id
            line_bot_api.push_message(user_id,TextSendMessage(text=msg))
        except:
            room_id = event.source.room_id
            line_bot_api.push_message(room_id,TextSendMessage(text=msg))

def Usage(event):
    push_msg(event,"     🤪🤪 查詢方法 🤪🤪     \
                    \n\
                    \n🌝小幫手可以查詢油價➡匯率➡股價\
                    \n\
                    \n🌝 油價通知 ➡➡➡ 輸入查詢油價\
                    \n🌝 匯率兌換 ➡➡➡ 輸入查詢匯率\
                    \n🌝 匯率通知 ➡➡➡ 換匯TWD/USD\
                    \n🌝 股價查詢 ➡➡➡ 輸入#股票代號")