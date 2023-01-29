import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
model = tree.DecisionTreeClassifier()

df = pd.read_csv('Spartahack\db_train.csv')

prog = df[['prognosis']]

input_ = df.drop('prognosis', axis='columns')
le_prog = LabelEncoder()

prog['prog_new'] = le_prog.fit_transform(prog['prognosis'])
# prog_test['prog_new_test'] = le_prog_test.fit_transform(prog_test['prognosis'])


prog_new = prog.drop('prognosis', axis='columns')

model.fit(input_, prog_new)

sc = model.score(input_, prog_new)