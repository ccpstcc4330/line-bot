from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('RYsDjzo4ItnB6+HSgWcElgfhb/gt8KTHmjMTcwUsJp35Yuk+hi4T67z10oAR6BzwXu5SkVfO7BtS6RP4MgmGo8POI/6N82P4Sxt4nK5JMIl6FpTeZ4sNRv9+W1GCWL3/ZAMNqugk7jKeSO195wPaYQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3dec617704f692bda86984c2c9c1bcfa')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '晚點再請小編回覆喔!'

    if msg in == ['hi' , 'HI']:
        r = 'HI'
    elif msg == '你好嗎':
        r = '很好啊，你呢?'
    elif msg == '你是誰?':
        r = '我是機器寇蒂!'
    elif '訂餐' in msg:
        r = '請問要訂什麼呢'
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()