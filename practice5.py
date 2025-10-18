import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
# print(train.head(10))
women = train.loc[train.Sex == 'female']['Survived']
rate_women = sum(women)/len(women)
# print(rate_women*100)
print(f"{rate_women*100:.2f}%")

men = train.loc[train.Sex == 'male']['Survived']
rate_men = sum(men)/len(men)
print(f"{rate_men*100:.2f}%")
