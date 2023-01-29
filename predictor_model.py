import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
import numpy as np

model = tree.DecisionTreeClassifier()

df = pd.read_csv('Spartahack\db_train.csv')

prog = df[['prognosis']]

input_ = df.drop('prognosis', axis='columns')
le_prog = LabelEncoder()

prog['prog_new'] = le_prog.fit_transform(prog['prognosis'].values)

prog_new = prog.drop('prognosis', axis='columns')


model.fit(input_, prog_new)

symptoms_list = ['headache','itching','skin_rash','blister','breathlessness'] # Fixed for Presenting
le_symptoms = LabelEncoder()

#Encode the symptoms_list
symptoms_list_encoded = le_symptoms.fit_transform(symptoms_list)


symptoms_df = pd.DataFrame(np.zeros((1, len(input_.columns))), columns=input_.columns)
symptoms_df[input_.columns[symptoms_list_encoded]] = 1


predicted_disease = le_prog.inverse_transform(model.predict(symptoms_df))
print(predicted_disease)
