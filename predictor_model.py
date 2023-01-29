# Telediagnosis.ai
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from gpt import gpt, speech_to_text
import pickle

def prediction_rf():
    model = RandomForestClassifier()

    df = pd.read_csv('C:\\Users\\Krish\\Desktop\\PROJECT\\Spartahack\\db_train.csv')

    prog = df[['prognosis']]

    input_ = df.drop('prognosis', axis='columns')
    le_prog = LabelEncoder()

    prog['prog_new'] = le_prog.fit_transform(prog['prognosis'].values)

    prog_new = prog.drop('prognosis', axis='columns')


    model.fit(input_, prog_new)


    # Make a list of all symptoms
    SYMPTOM_LIST = []
    for i in df:
        if i != 'prognosis':
            SYMPTOM_LIST.append(i)

    print('Please tell me your symptoms. The more expressive you are, the better I can diagnose you')

    rec_text = speech_to_text()

    print('Recognized Speech:', rec_text)

    if rec_text:
        symptoms_list = gpt(f'Assume that you have to return a Python list of symptoms from {SYMPTOM_LIST} based on this prompt. {rec_text}. Send a list of symptoms and nothing else.')
        symptoms_list = eval(symptoms_list)
    # symptoms_list = ['itching','skin_rash','blister','breathlessness'] # Fixed for Presenting
    le_symptoms = LabelEncoder()

    #Encode the symptoms_list
    symptoms_list_encoded = le_symptoms.fit_transform(symptoms_list)


    symptoms_df = pd.DataFrame(np.zeros((1, len(input_.columns))), columns=input_.columns)
    symptoms_df[input_.columns[symptoms_list_encoded]] = 1


    predicted_disease = le_prog.inverse_transform(model.predict(symptoms_df))
    return predicted_disease[0]
