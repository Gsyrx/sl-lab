import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')

print("Head of Dataset")
print(df.head(5))

print("Description of dataset")
print(df.describe())

print("Information of dataset")
print(df.info())

df.drop(['Parch','PassengerId','Name','Ticket'], axis=1, inplace=True)
print(df.head(10))

df["Age"] = df["Age"].fillna(0)
print(df.head(10))


df ['Survived'] = df ['Survived'].map({
    0: 'Died',
    1: 'Alive'
})
print(df.head(5))

ax = sns.countplot(data = df, x = 'Pclass', hue = 'Survived', palette = 'Set1')
ax.set(title = 'Passenger status (Survived/Died) against Passenger Class',
       xlabel = 'Passenger Class', ylabel = 'Total')
plt.show()   


ax = sns.countplot(data = df, x = 'Sex', hue = 'Survived', palette = 'Set2' )
ax.set(title = 'Total Survivors According to Sex', xlabel = 'Sex', ylabel='Total')
plt.show()




interval = (0,18,35,60,120)
categories = ['Children','Teens','Adult', 'Old']
df['Age_cats'] = pd.cut(df.Age, interval, labels = categories)

ax = sns.countplot(data = df,x = 'Age_cats', hue = 'Survived', palette = 'Set3')

ax.set(xlabel='Age Categorical', ylabel='Total',
       title="Age Categorical Survival Distribution")
plt.show()