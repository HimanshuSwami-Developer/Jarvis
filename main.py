from config import key
import requests
from command import input_instruction


def chat1(chat):
    messages = [] #list that will contain all the messages of conversation
    system_mesage = "You are an AI chatbot, your name is jarvis"
    message = {"role":"user", "parts" : [{"text":system_mesage+" "+chat}]    }
    messages.append(message)
    data = {"contents":messages} 
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key 
    response = requests.post(url, json=data)

    t1 = response.json()
    #print(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)

#chat = input_instruction()
#print(chat + "testing......")
#chat = input("Enter the query - ")
chat1("who is ms dhoni")    