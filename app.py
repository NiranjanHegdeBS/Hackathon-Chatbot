from flask import Flask, request, jsonify
import json
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Customer Support Chatbot"

start = 1 
chatbot_qa = json.loads(open('chatbot.json').read())

@app.route("/api/messages",methods=["POST","GET"])
def chatbot_response():
    global start
    if(start):
        question = chatbot_qa[0]["que"]
        follow_up = chatbot_qa[0]["options"]
        response_msg = {"question":question,"follow_up":follow_up}
        start = 0
        return jsonify(response_msg)
    else:
        print(request.get_json())
        return(jsonify(request.get_json()))
    # msg = request.form["msg"]
    # if(sentiment_analyser(msg) == "POSITIVE"):
    #     response_msg = {}
        



if __name__ == "__main__":
    app.run()