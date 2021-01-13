import pandas as pd
import matplotlib.pyplot as plt
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


ax = sns.countplot(data=df,x="test preparation course",hue='gender',palette='Set3')
ax.set(title="Course completion based on gender", xlabel='Course', ylabel='Total')
plt.show()

ax = sns.countplot(data=df,x="race/ethnicity",hue="gender",palette="Set2")
ax.set(title="Total number of male and female students belonging to each group", xlabel="Groups", ylabel="Total")
plt.show()


interval=(0,40,50,60,75)
categories = ["Fail", "2nd class","1st class","Distinction"]
df["Marks_cats"]=pd.cut(df.mathscore,interval,labels=categories)
ax=sns.countplot(data=df,x="Marks_cats",hue="gender",palette="Set1")
ax.set(title="Marks categorisation for math",xlabel="Categories",ylabel="Number of students")
plt.show()