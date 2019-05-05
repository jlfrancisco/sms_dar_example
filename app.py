from flask import Flask, jsonify
import requests

app = Flask(__name__)

secret_key = "dQvcvocmTmGeyFzjRcDTG0SAYyHP"

@app.route("/hello")
def hello():
    return 'Hello world!'


@app.route("/sms/<string:phone_number>")
def send_sms(phone_number):
    r = requests.post(
        "https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B221777240843/requests",
        json = {
            'outboundSMSMessageRequest': {
                "address": "tel:+221"+phone_number,
                "senderAddress": "tel:+221777240843",
                "outboundSMSTextMessage": {
                    "message": "Hello!!"
                }
            }
        },
        headers = {
            'Authorization': 'Bearer dQvcvocmTmGeyFzjRcDTG0SAYyHP',
            'Content-Type': 'application/json'
        }
    )
    if (r.status_code == 201):
        return jsonify(
            {
                'status': 'OK',
                'message': 'Le sms est bien acheminé!'
            }
        )
    return jsonify(
        {
            'status': 'KO',
            'message': 'Il y a un probleme'
        }
    )


if __name__=="__main__":
    app.run()


