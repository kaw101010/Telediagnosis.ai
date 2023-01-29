import openai
from config import API_KEY
from mlmodel import df
import pyttsx3
import speech_recognition

SYMPTOM_LIST = []
for i in df:
    if i != 'prognosis':
        SYMPTOM_LIST.append(i)

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


disease_list = ['headache', 'insomnia','throat_pain']

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

print('OK NOW SPEAK!!')
recognized_speech = speech_to_text()

if recognized_speech:
    list_symptoms = gpt(f'Assume that you have to return a Python list of symptoms from {SYMPTOM_LIST} based on this prompt. {recognized_speech}. Send a list of symptoms and nothing else.')
# try:
#     list_symptoms = eval(list_symptoms)
# except TypeError:
#     print('Please express your symtoms more efficiently.')
print(list_symptoms)

