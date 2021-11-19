from flask import Flask, request, jsonify
import json
from flask_cors import CORS, cross_origin
#from utils import MessageAnalysis as MessageAnalysis
app = Flask(__name__)

cors = CORS(app,resources={r"/api/*": {"origins": "*"}})

app.config['CORS_HEADERS'] = 'Content-Type'

chatbot_qa = json.loads(open('chatbot.json').read())
username = "Mike"

@app.route("/")
def home():
    return "Welcome to Customer Support Chatbot"

@app.route("/api/messages",methods=["POST","GET"])
def chatbot_response():
    response_msg = {}

    if request.method == "GET":
        greeting = f"Hello {username}!"
        question = chatbot_qa[0]["que"]
        follow_up = chatbot_qa[0]["options"]
        response_msg = {"greeting":greeting,"question":question,"follow_up":follow_up}
        
    elif request.method == "POST":
        user_option_info = request.get_json()
        if "key" in user_option_info:
            key = -1
            for i in range(len(chatbot_qa)):
                if int(chatbot_qa[i]["id"]) == user_option_info["key"]:
                    key = i
                    break
                
            question = chatbot_qa[key]["que"]
            follow_up = chatbot_qa[key]["options"]
            response_msg = {"question":question,"follow_up":follow_up}

        # elif "message" in user_option_info:
        #     msg = user_option_info["message"]
        #     responseText = MessageAnalysis.MessageAnalyser(msg)
    
    return(jsonify(response_msg))
    
if __name__ == "__main__":
    app.run(host="0.0.0.0")