import openai
from config import API_KEY
import pyttsx3
import speech_recognition



def gpt(stext):
    openai.api_key = API_KEY
    response = openai.Completion.create(
        engine = "davinci-instruct-beta",
        prompt = stext,
        temperature = 0.1,
        max_tokens = 1000,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0
    )
    return response.choices[0].text



def speech_to_text():
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration = 0.1)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()
                # print("Recognized: ",text)
                return text
                
        except speech_recognition.UnknownValueError():
            recognizer = speech_recognition.Recognizer()
            continue





