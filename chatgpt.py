from revChatGPT.ChatGPT import Chatbot
import json


data = json.load(open('config_data.json', 'r')) # replace to config.json
chatbot = Chatbot(data,conversation_id=None, parent_id=None) 


def send_message_from_voice(message):
    response = chatbot.ask(message, conversation_id=None, parent_id=None) 
    return response


