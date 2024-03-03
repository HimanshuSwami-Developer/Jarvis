import speech_recognition as sr

listener = sr.Recognizer()

def input_instruction():
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            while True:
                speech = listener.listen(origin)
                instruction = listener.recognize_google(speech)
                instruction = instruction.lower()
                print(instruction)
                if "jarvis" in instruction:
                    instruction = instruction.replace('jarvis', "")
                    print(instruction)
                    return instruction
    except:
        print("Microphone not detected...")
        return ""
