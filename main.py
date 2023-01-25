import os

from initial_assistan import speak,takeCommand,wishMe
from chatgpt import send_message_from_voice

if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    clear()
    wishMe()
     
    while True:
        query = takeCommand().lower()
        content = send_message_from_voice(query)
        print(content)
        speak(content['message'])
        