from flask import Flask, request, jsonify
from main import sendmail

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/write", methods=['POST'])
def write():
    req = request.get_json()
    name = req["action"]["detailParams"]["Name"]["value"]
    title = req["action"]["detailParams"]["Title"]["value"]
    contents = req["action"]["detailParams"]["Contents"]["value"]
    sendmail(name, title, contents)
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "성공적으로 전송했습니다."
                    }
                }
            ]
        }
    }

    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5000)
