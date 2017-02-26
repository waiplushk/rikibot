from flask import Flask, request
import json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "<p>Hello World!</p>"

@app.route('/callback', methods=['POST'])
def callback():
    json_line = request.get_json()
    json_line = json.dumps(json_line)
    decoded = json.loads(json_line)
    user = decoded['result'][0]['content']['from']
    text = decoded['result'][0]['content']['text']
    #print(json_line)
    print("使用者：",user)
    print("內容：",text)
    sendText(user,text)
    return ''

def sendText(user, text):
    LINE_API = 'https://trialbot-api.line.me/v1/events'
    CHANNEL_ID = '1503034805'
    CHANNEL_SERECT = 'db2291b0611e74dfee6b81d66407e509'
    MID = 'ceTNL2J4uc+jYPwFzET135bsgOW19/rYwQHyN4Z6w2WZSY0qs3Vu/DvOZzfeg7Y6bFmR1WsjC5v/dBMGGvkjhhIrvdkym45oToPNjnfHBX9iHAQUzN7Rdi8yx1l1tyxXOnxfbVyFrGuIftYg2GwQrgdB04t89/1O/w1cDnyilFU='

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'X-Line-ChannelID': CHANNEL_ID,
        'X-Line-ChannelSecret': CHANNEL_SERECT,
        'X-Line-Trusted-User-With-ACL': MID
    }

    data = json.dumps({
        "to": [user],
        "toChannel":1383378250,
        "eventType":"138311608800106203",
        "content":{
            "contentType":1,
            "toType":1,
            "text":text
        }
    })

    #print("送出資料：",data)
    r = requests.post(LINE_API, headers=headers, data=data)
    #print(r.text)

if __name__ == '__main__':
     app.run(debug=True)
