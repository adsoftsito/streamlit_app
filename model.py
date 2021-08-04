import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction import DictVectorizer

df = pd.read_csv('dataset.csv')
print (df.size)
print (df.dtypes)

print (df.isnull().isnull().sum())

df[df.sex == 'F'].size
df[df.sex == 'M'].size
df_names = df
print (df_names)

df_names.sex.replace({'F':0,'M':1},inplace=True)
Xfeatures =df_names['name']

cv = CountVectorizer()
X = cv.fit_transform(Xfeatures)

from sklearn.model_selection import train_test_split

X
y = df_names.sex
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

from sklearn.naive_bayes import MultinomialNB 

clf = MultinomialNB()
clf.fit(X_train,y_train)
clf.score(X_test,y_test)

def predict(a):
    test_name = [a]
    vector = cv.transform(test_name).toarray()
    if clf.predict(vector) == 0:
        print("Female")
    else:
        print("Male")

#from sklearn.externals import joblib

import joblib

naiveBayesModel = open("model/naivemodel.pkl","wb")
joblib.dump(clf,naiveBayesModel)
naiveBayesModel.close()

