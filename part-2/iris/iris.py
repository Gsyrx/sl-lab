import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('iris.csv')

print("Head of dataset")
print(df.head(5))

print("Description of dataset")
print(df.describe())

print("Information of dataset")
print(df.info())

df.drop(['Sepal_Length'], axis=1, inplace=True)
print(df.head(5))


ax = sns.countplot(data = df,x = ' Sepal_Width',hue = 'Class',palette='Set1',)
ax.set(title='Flowers of each specie',xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()

ax = sns.countplot(data = df,x = ' Petal_Length',hue = 'Class',palette='Set1',)
ax.set(title='Flowers of each specie',xlabel='Petal Length',ylabel='No. of flowers')
plt.show()

ax = sns.countplot(data = df,x = ' Petal_Width',hue = 'Class',palette='Set1',)
ax.set(title='Flowers of each specie',xlabel='Petal Width',ylabel='No. of flowers')
plt.show()

