import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score


data_heart = pd.read_csv('heart.csv')
data_diabetes = pd.read_csv('diabetes.csv')
data_cancer = pd.read_csv('cancer.csv')
data_liver = pd.read_csv('liver.csv')
corr = data_heart.corr()

#code for Heart disease
dataset_heart = data_heart.copy()
X_h = dataset_heart.drop(['target'], axis=1)
y_h = dataset_heart['target']
X_h_train, X_h_test, y_h_train, y_h_test = train_test_split(X_h, y_h, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=20)
model.fit(X_h_train, y_h_train)
pred = model.predict(X_h_test)
confusion_matrix(y_h_test, pred)
print(f"Accuracy of current model is {round(accuracy_score(y_h_test, pred) * 100, 2)}%")
print(y_h_test)
print("----------")
print(pred)
print("Diagnoses for heart disease is done------------")
#Code for diabetes
X_b = data_diabetes.iloc[:,:-1]
y_b = data_diabetes['Outcome']
X_b_train, X_b_test, y_b_train, y_b_test = train_test_split(X_b, y_b, test_size = 0.2, random_state = 10)
model_b = RandomForestClassifier(n_estimators=20)
model_b.fit(X_b_train, y_b_train)
pred_b = model_b.predict(X_b_test)
print("Diagnoses for Diabetes is")
print(accuracy_score(y_b_test, pred_b)*100)
print(y_b_test)
print(pred_b)

#Code for Cancer Disease
"""dataset_c = data_cancer
dataset_c['diagnosis'].replace(['M','B'], [1,0], inplace = True)
dataset_c.drop(['id','symmetry_se','smoothness_se','texture_se','fractal_dimension_mean'], axis = 1, inplace = True)
X_c = dataset_c.drop('diagnosis', axis = 1)
y_c = dataset_c['diagnosis']
X_c_train, X_c_test, y_c_train, y_c_test = train_test_split(X_c, y_c, test_size = 0.2, random_state = 42)
model_c = RandomForestClassifier(n_estimators=20)
model_c.fit(X_c_train, y_c_train)
confusion_matrix(y_c_test, model_c.predict(X_c_test))
pred_c = model_c.predict(X_c_test)
print(f"Accuracy is {round(accuracy_score(y_c_test, pred_c )*100,2)}")"""

#Code for Liver Disease
"""data_liver['Dataset'] = data_liver['Dataset'].replace([2,1],[1,0])
data_liver['Dataset'].head()
data_l = pd.get_dummies(data_liver, columns = ['Gender'], drop_first = True)
X_l = data_l.drop('Dataset', axis = 1)
y_l = data_l['Dataset']
X_l_train, X_l_test, y_l_train, y_l_test = train_test_split(X_l, y_l, test_size = 0.1, random_state = 42)
model_l = RandomForestClassifier(n_estimators=20)
model_l.fit(X_l_train, y_l_train)
confusion_matrix(y_l_test, model.predict(X_l_test))
pred_l = model.predict(X_l_test)
print(f"Accuracy is {round(accuracy_score(y_l_test, pred_l )*100,2)}")"""