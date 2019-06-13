from flask import Flask,request
import random
from pymessenger.bot import Bot
from CrappieAi import Small_talk
import random
app = Flask(__name__)
talk = Small_talk()
bot = Bot('Page_token')
@app.route('/',methods=["GET","POST"])
def webhook():
    if request.method == "GET":
        token_sent = request.args.get('hub.verify_token')
        return verify_fb_token(token_sent)

    else:
        data = request.get_json()
        print(data)
        for event in data['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        # provoke get_message by assign it respone_sent_text by taking user query
                        response_sent_text = get_message(message['message'].get('text'))
                        #send back the message of response_send_text
                        if response_sent_text[1] == 1:
                            #send the text and option to choose
                            send_message(recipient_id, response_sent_text[0])
                            try:
                                bot.send_button_message(recipient_id,"This what I can do:",[{"type":"postback","title":"Working with File","payload":"idontknow"},{"type":"postback","title":"Vkirirom","payload":"idontknow"},{"type":"postback","title":"Pokemon","payload":"idontknow"}])
                            except:
                                send_message(recipient_id, "Sorry something went wrong")
                        #it will only send the respone_text
                        elif response_sent_text[1] == 0:
                            send_message(recipient_id, response_sent_text[0])

                    #if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
        return 'message procced'

def verify_fb_token(token_sent):
    if token_sent == "idontknow":
        return request.args.get("hub.challenge")
    return "Invalid verifiation token"


#provoke Talk in order to send a nutural message to user
def get_message(message):
    
    return talk.get_message(message)

#uses PyMessenger to send response to user
def send_message(recipient_id,respone):
    bot.send_text_message(recipient_id,respone)
    return 'success'

if __name__ == "__main__":
    app.run(debug=True)