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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()