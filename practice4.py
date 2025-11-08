import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

train = pd.read_csv("train.csv")
train['Gender'] = train['Sex'].replace({'male': 1, 'female': 0})
variables=train[["Pclass","Gender"]]
output=train["Survived"]

model=LogisticRegression().fit(variables,output)

y_intercept=model.intercept_
coefficients=model.coef_
print(y_intercept)
print(coefficients[0])

e=2.71828182846
def calculateSurvival(Pclass,Gender):
    z=y_intercept+coefficients[0][0]*Pclass+coefficients[0][1]*Gender
    sigmoid=1/(1+e**-z)
    return (sigmoid>0.5)
        


test=pd.read_csv("test.csv")
test['Gender'] = test['Sex'].replace({'male': 1, 'female': 0})
test["Survived"]=calculateSurvival(test["Pclass"],test["Gender"]).astype(int)
answer=test.get(["PassengerId","Survived"])
print(answer.head())

correct=0
wrong=0
def AccuracyCount(givenAnswer,correctAnswer):
    if givenAnswer==correctAnswer:
        correct+=1
    else:
        wrong+=1


gender=pd.read_csv("gender_submission.csv")
AccuracyCount(test["Survived"],gender["Survived"])
print(f"The accuracy of the model is:{correct/(wrong+correct)}")



