#import pandas as pd
#test = pd.read_csv("test.csv")
#gender_submission=pd.read_csv("gender_submission.csv")
#a=test.get(["PassengerId","sex"])
#print(a)
# print(test.head(10))
# print(test.columns)
# print(test.columns[2])
# a=test.get(["PassengerId","Pclass"])
# print(a)
# train = pd.read_csv("train.csv")
# b = train.get(["PassengerId","Survived"])
# a.merge(right=b,how="left",on="PassengerId")
# print(b)

import pandas as pd

# Load the data and select specific columns
test = pd.read_csv("test.csv")[["Sex", "PassengerId"]]
gender=pd.read_csv("gender_submission.csv")

# Set 'Survived' to 1 if Sex is 'female', otherwise 0
test['Survived'] = (test['Sex'] == 'male').astype(int)
test=test.drop(columns="Sex")
#print(test.head())
#print(gender.head())

differences=test.compare(gender)
print(differences)