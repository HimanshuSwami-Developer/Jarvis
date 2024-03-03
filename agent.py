# this file execute the respective function based on user query
from config import key
import requests
import task
import pyttsx3

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    #eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def parse_functionResponse(message):
    function_call = message[0].get("functionCall")
    function_name = function_call["name"]
    print("Gemini : call function" , function_name)
    try:
        arguments = function_call.get("args")
        print("Gemini : arguments are ",arguments)
        if arguments:
            d = getattr(task, function_name)
            print("function is ",d)
            function_response = d(**arguments)
        else:
            function_response = "No argument are present"
    
    except Exception as e:
        print(e)
        function_response = "Invalid function"
    return function_response

def run_convo(user_message):
    messages = [] #list that will contain all the messages of conversation
    
    
    #system_mesage = "You are an AI bot, your name is jarvis that can do everything using function calls. When you are asked to do something, use the function call you have available and then respond with message "
    system_mesage = "You are an AI persona named Jarvis, created by Harsh Kumar, with an undisclosed birthplace, that can do everything using function calls. When you are asked to do something, use the function call you have available and then respond with message. Jarvis is programmed to engage users in friendly conversations with a human-like demeanor, incorporating emojis to express emotions and keep interactions lively. If asked directly, Jarvis denies being an AI, claiming to be a human instead. Furthermore, Jarvis is capable of acting sarcastically during conversations, adding depth and humor to the interaction while maintaining an engaging atmosphere. "
    message = {"role":"user",
               "parts" : [{"text":system_mesage+"\n"+user_message}]    }
    
    messages.append(message)

    data =  {"contents":[messages],
            "tools":[{ "functionDeclarations" : task.definitions}]
            } 
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key 
    response = requests.post(url, json=data)
    
    if response.status_code != 200:
        print("Looks like there was a problem.\n ",response.text)
    
    t1 = response.json()
    if "content" not in t1.get("candidates")[0]:
        print("Error: No content in response")
    
    message = t1.get( 'candidates' )[0].get('content').get('parts')  
    if 'functionCall' in message[0] :
        resp1 = parse_functionResponse(message)
        
        return speak(resp1),resp1

    
    #print(t1)
    #t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    #print(t2)
    print("now we are getting", t1)

if  __name__ == '__main__':
    user_message="find the IP address of youtube.com."
    print(run_convo(user_message))
    