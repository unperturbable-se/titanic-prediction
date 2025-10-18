import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
a=train.groupby(["Sex","Survived"]).mean()
print("Average rate of Survival by Sex")
print(a)
male = a["male"]
female = a["female"]
print(f"The Average is for male {male/890} and female {female/890}")
