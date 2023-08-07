from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('92kcy07IM75HrTqA3x+nCn61QmpKr0I5c1gH3Dumn5MR8DP1876/38wqBFlF/1KqP+R+cjzpqvxLD1NELcik69B92V8+k4Wt0ZroHxEoL5HZ19/nT7RC6v3j08G6AFd2/sFxfJy2tsy84WGEbNNrwQdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('8cfd13f4a443434527574c3c6b80b0ab')