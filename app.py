from flask import Flask, request, jsonify
import json
app = Flask(__name__)

chatbot_qa = json.loads(open('chatbot.json').read())

@app.route("/")
def home():
    return "Welcome to Customer Support Chatbot"

@app.route("/api/messages",methods=["POST","GET"])
def chatbot_response():
    response_msg = {}

    if request.method == "GET":
        question = chatbot_qa[0]["que"]
        follow_up = chatbot_qa[0]["options"]
        response_msg = {"question":question,"follow_up":follow_up}
        
    elif request.method == "POST":
        user_option_info = request.get_json()
        key = -1
        for i in range(len(chatbot_qa)):
            if int(chatbot_qa[i]["id"]) == user_option_info["key"]:
                key = i
                break
              
        question = chatbot_qa[key]["que"]
        follow_up = chatbot_qa[key]["options"]
        response_msg = {"question":question,"follow_up":follow_up}
    
    return(jsonify(response_msg))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")