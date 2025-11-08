import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
# a=train.groupby(["Sex","Survived"]).mean()
# print("Average rate of Survival by Sex")
# print(a)
# male = a["male"]
# female = a["female"]
# print(f"The Average is for male {male/890} and female {female/890}")




#----------------------------------MODEL ig percentage chances btane hain 

import pandas as pd
test=pd.read_csv("test.csv")

answer=pd.get(["PassengerId"])

for i in range(test):
    if test[i]["Sex"]=="male":
        for row in answer:
            if(row[""])

