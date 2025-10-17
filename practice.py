import pandas as pd
test = pd.read_csv("test.csv")
# print(test.head(10))
# print(test.columns)
# print(test.columns[2])
a=test.get(["Pclass"])
# print(a)
train = pd.read_csv("train.csv")
b = train.get(["PassengerId","Survived"])
# print(b)
c = a+b
print(c)



