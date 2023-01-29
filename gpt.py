import openai
from config import API_KEY
from new import df

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

list_symptoms = gpt(f'Assume that you have to return a Python list of symptoms from {SYMPTOM_LIST} based on this prompt. I feel sleepy and tired. My stomach is hurting me. Send a list of symptoms and nothing else.')
try:
    list_symptoms = eval(list_symptoms)
except TypeError:
    print('Please express your symtoms more efficiently.')


