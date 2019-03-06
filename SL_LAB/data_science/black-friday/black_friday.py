import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

friday_df = pd.read_csv('test.csv') # a 
print(friday_df.head()) # b 
friday_df = friday_df.drop(['User_ID', 'Product_ID', 'Stay_In_Current_City_Years'],axis=1) # c

friday_df['City_Category']=friday_df['City_Category'].fillna('B') # d

friday_df['City_Category']=friday_df['City_Category'].map({'A':'Metro Cities', 'B':'Small Towns', 'C':'Villages'}) # e

#friday_df['Product_Category_1']=friday_df['Product_Category_1'].fillna('Baseball Caps') # f
#friday_df['Product_Category_2']=friday_df['Product_Category_2'].fillna('Wine Tumblers') # f
#friday_df['Product_Category_3']=friday_df['Product_Category_3'].fillna('Pet Raincoats') # f

friday_df['Marital_Status'] = friday_df['Marital_Status'].map({1:'Married',0:'Un-Married'}) # g

a=sns.countplot(x='Gender', hue='City_Category', palette='Set1', data=friday_df) # h(ii)
a.set(title='gender VS City_Category', xlabel='gender', ylabel='total')
print(pd.crosstab(friday_df['Gender'], friday_df['City_Category']))
plt.show()

b=sns.countplot(x='Gender', hue='Product_Category_1', palette='Set1', data=friday_df) # h(i)
a.set(title='gender VS Product_Category_1', xlabel='gender', ylabel='total')
print(pd.crosstab(friday_df['Gender'], friday_df['Product_Category_1']))
plt.show()

a=sns.countplot(x='Gender', hue='Product_Category_2', palette='Set2', data=friday_df) # h(i)
a.set(title='gender VS Product_Category_2', xlabel='gender', ylabel='total')
print(pd.crosstab(friday_df['Gender'], friday_df['Product_Category_2']))
plt.show()
