import pandas as pd
import numpy as np

df = pd.read_csv("blackfri.csv")
print("Head of dataset")
print(df.head(5))

print("Description of dataset")
print(df.describe())

print("Information of dataset")
print(df.info())

df.drop(['User_ID','Product_ID','Age','Occupation','Stay_In_Current_City_Years','Purchase'],axis=1,inplace=True)
print(df.head(5))


df['City_Category'] = df['City_Category'].fillna("A")
print(df.head(5))

df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))

df.rename(columns={'City_Category':'City Category'},inplace=True)
print(df.head(5))

df['Marital_Status'] = df['Marital_Status'].map({1:'Married',0:'Un-Married'})
print("New Marital Status")
print(df['Marital_Status'])

import matplotlib.pyplot as plt
import seaborn as sns

print("<-------Data Visualisation------->")
print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Pet_Raincoats))

ax = sns.countplot(data=df,x='Gender',hue='Pet_Raincoats',palette='Set2')
ax.set(title='Male and Female who bought Pet_Raincoats',xlabel='Gender',ylabel='Count')
plt.show()


ax = sns.countplot(data=df,x='Gender',hue='City Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()