import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("StudentsPerformance.csv")
print("Head of dataset")
print(df.head(15))

print("Description of dataset")
print(df.describe())

print("Information of dataset")
print(df.info())

df.drop(['lunch'],axis=1,inplace=True)
print(df.head(5))

df["parental level of education"] = df["parental level of education"].fillna("Not applicable")
print(df.head(5))

df["race/ethnicity"] = df["race/ethnicity"].map({"group A": "Asian students",
"group B": "American students","group C": "European students","group D": "Indian students","group E": "African students"})
print(df.head(5))

ax = sns.countplot(data=df,x="test preparation course",hue='gender',palette='Set3')
ax.set(title="Course completion based on gender", xlabel='Course', ylabel='Total')
plt.show()

ax = sns.countplot(data=df,x="race/ethnicity",hue="gender",palette="Set2")
ax.set(title="Total number of male and female students belonging to each group", xlabel="Groups", ylabel="Total")
plt.show()