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



interval = (0,1,2,4)
category = ['<1','1 to 2','>2']
df['Petal_Catg'] = pd.cut(df[' Petal_Width'],interval,labels=category)

ax = sns.countplot(data = df,x = 'Petal_Catg',hue = 'Class',palette='Set1',)
ax.set(title='Petal Width',xlabel='Category of Petals',ylabel='No. of flowers')
plt.show()



ax = sns.countplot(data = df[df['Class'] == 'Iris-setosa'],x = ' Sepal_Width',palette='Set1')
ax.set(title='Iris-setosa',xlabel='Sepal Width',ylabel='No. of flowers')
plt.show()


