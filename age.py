import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
#print(train.columns)
#b = pd.read_csv("gender_submission.csv")
#train = train.merge(right=b, on="PassengerId", how="left")
#train = train[train["Sex"] != "male"]
survival_rate = train.groupby("Pclass")["Survived"].mean()*100
# print("Survival Rate by Pclass: ")
# print(survival_rate.head())
# survival_rate.plot(kind="hist")
# plt.title("Titanic Survival Rate by Pclass")
# plt.xlabel("Pclass")
# plt.ylabel("Survival Rate")
# plt.show() 
# print(survival_rate.head())
survival_rate.plot(kind="bar", color="skyblue", edgecolor="black")

plt.title("Titanic Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Average Survival Rate")
plt.xticks(rotation=0)
plt.show()