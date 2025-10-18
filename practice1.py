
import pandas as pd
import matplotlib.pyplot as plt
train = pd.read_csv("train.csv")
#print(train.columns)
#b = pd.read_csv("gender_submission.csv")
#train = train.merge(right=b, on="PassengerId", how="left")
survival_rate = train.groupby("Sex")["Survived"].sum()
print("Survival Rate by Gender: ")
print(survival_rate.head())
survival_rate.plot(kind="bar")
plt.title("Titanic Survival Rate by Gender")
plt.xlabel("Sex")
plt.ylabel("Survival Rate (%)")
plt.xticks(rotation=0)
plt.show() 
#male_survived = train[(train["Sex"] == "male") & (train["Survived"] == 1)].shape[0]
#print("Number of males who survived:", male_survived) 
#female_survived = train[(train["Sex"] == "female") & (train["Survived"] == 1)].shape[0]
#print("Number of females who survived:", female_survived) 

