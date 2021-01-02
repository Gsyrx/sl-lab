import pandas as pd
import numpy as np

df = pd.read_csv("blackfri.csv")
print("<-----Data Information----->")
print("Head of Dataset")
print(df.head(5))
print("Head of Dataset")
print(df.describe())
print(df.info())

# Removing unnecessary features 
df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace=True)
print(df.head(5))
   

# Manipulate data by replacing empty column values in ‘City_Category’ 
# with a default value for the city
print("Filling empty values")
df['City_Category'] = df['City_Category'].fillna("A")
print(df.head(5))


# Convert the attribute ‘City_Category’ 
# ‘A’ to be ‘Metro Cities’, ‘B’ to be ‘Small Towns’ ,  ‘C’ to be ‘Villages’
print("Mapping values/attributes in City_Category to types")
df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))


print("Renaming the column names")
df.rename(columns={'Product_Category_1':'Baseball_Caps','Product_Category_2':'Wine_Tumblers','Product_Category_3':'Pet_Raincoats'},inplace=True)
print(df.head(5))


print("Mapping values/attributes in Marital Status to types")
df['Marital_Status'] = df['Marital_Status'].map({1:'Married',0:'Un-Married'})
print(df.head(5))


import matplotlib.pyplot as plt
import seaborn as sns
print("<-------Data Visualisation------->")
print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Pet_Raincoats))

ax = sns.countplot(data=df,x='Gender',hue='Pet_Raincoats',palette='Set2')
ax.set(title='Male and Female who bought Pet_Raincoats',xlabel='Gender',ylabel='Count')
plt.show()


ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()