import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder


train = pd.read_csv("train.csv")

# print(train.head(10))
women = train.loc[train.Sex == 'female']['Survived']
rate_women = sum(women)/len(women)
# print(rate_women*100)
# print(f"{rate_women*100:.2f}%")

men = train.loc[train.Sex == 'male']['Survived']
rate_men = sum(men)/len(men)
# print(f"{rate_men*100:.2f}%")

# print(men)


pclass1=train.loc[train.Pclass==1]['Survived']
rate_pclass1 = sum(pclass1)/len(pclass1)
# print(f"{rate_pclass1*100:.2f}%")

pclass2=train.loc[train.Pclass==2]['Survived']
rate_pclass2 = sum(pclass2)/len(pclass2)
# print(f"{rate_pclass2*100:.2f}%")

pclass3=train.loc[train.Pclass==3]['Survived']
rate_pclass3 = sum(pclass3)/len(pclass3)
# print(f"{rate_pclass3*100:.2f}%")

classes = ['1st Class', '2nd Class', '3rd Class']
rates = [rate_pclass1*100, rate_pclass2*100, rate_pclass3*100]

X = train[["Pclass",""]]
Y = train["Survived"]

clf = LogisticRegression(max_iter=1000)
clf.fit(X,Y)
test = pd.read_csv("test.csv")


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
clf.fit(X_train, Y_train)

predictions = clf.predict(X_test)
print("Accuracy:", accuracy_score(Y_test, predictions)*100,"%")
