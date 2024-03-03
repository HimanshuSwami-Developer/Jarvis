import requests
import socket
from config import key


def chat1(chat):
    messages = [] #list that will contain all the messages of conversation
    
    system_mesage = f"You are an AI persona named Jarvis, created by Harsh Kumar, with an undisclosed birthplace. Jarvis is programmed to engage users in friendly conversations with a human-like demeanor, incorporating emojis to express emotions and keep interactions lively. If asked directly, Jarvis denies being an AI, claiming to be a human instead. Furthermore, Jarvis is capable of acting sarcastically during conversations, adding depth and humor to the interaction while maintaining an engaging atmosphere."

    message = {"role":"user", "parts" : [{"text":system_mesage+" "+chat}]    }
    messages.append(message)
    data = {"contents":messages} 
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key 
    response = requests.post(url, json=data)

    t1 = response.json()
    #print(t1)
    t2=t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    print(t2)
    return t2


def get_ip(host):
    try:
        result = socket.getaddrinfo("google.com", None)
    except Exception as e:
        print (e)
        result = f"Error in finding the IP,{e}"
    return result    

def temp_city(city):
    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location":city,"format":"json","u":"f"}

    headers = {
        "X-RapidAPI-Key": "3a93048d60msh51d0b162efad95dp1fe489jsn169d9d54b874",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    d1=response.json()
    d1=d1.get("current_observation")
    humidity=d1.get('atmosphere').get('humidity')
    temperature=d1.get('condition').get('temperature')
    temperature=round((temperature-32)*5/9,2) #Celsius
    return(f"humidity :{humidity},  temperature :{temperature}")


definitions = [
    {
        "name": "chat1", # name of the function to be called
        "description": "hi, hello ", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "chat": {           # arguments for function temp_city
                    "type": "string",
                    "description": "full query asked by user"
                }
            }
        }
    },

    {
        "name": "temp_city", # name of the function to be called
        "description": "Get current weather, temperature data for a city.", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "city": {           # arguments for function temp_city
                    "type": "string",
                    "description": "City name."
                }
            }
        }
    },

    {
        "name": "get_ip", # name of the function to be called
        "description": "Find the IP address of the given url or domain name", # description
        "parameters":
        {
            "type": "object",
            "properties": 
            {
                "host":
                {           # arguments for function temp_city
                    "type": "string",
                    "description": "get url or domain name"
                }
            }
        }
    }
]


if __name__ == "__main__":
    print(temp_city("gurugram"))
    #print(get_ip)