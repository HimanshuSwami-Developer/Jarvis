import speech_recognition as sr

listener = sr.Recognizer()
def input_instruction():
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        while True:
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            #instruction = instruction.lower()
            print(instruction)
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "")
                print(instruction)
                return instruction
            return instruction
   
if __name__ == "__main__":
    input_instruction()
#input_instruction()