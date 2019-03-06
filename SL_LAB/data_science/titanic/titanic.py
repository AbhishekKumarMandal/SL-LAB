import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('train.csv')

# data manipulation 1
titanic_df['Survived']=titanic_df['Survived'].map({0:'died', 1:'survived'})
#print(titanic_df.head())

# data manipulation 2
titanic_df=titanic_df.drop(['SibSp', 'Parch', 'Ticket', 'Fare'],axis=1)
#print(titanic_df.head())

#data manipulation 3
titanic_df['Pclass']=titanic_df['Pclass'].map({1:'Luxury Class',2:'Economy Class', 3:'Lower Class'})
#print(titanic_df.head(20))

# data manipulation 4
titanic_df['Embarked']=titanic_df['Embarked'].fillna('S')
titanic_df['Cabin']=titanic_df['Cabin'].fillna('A26')
titanic_df['Age']=titanic_df['Age'].fillna(30)
#print(titanic_df.head(20))

# data manipulation 5
titanic_df['Embarked']=titanic_df['Embarked'].map({'S':'southampton','C':'cherbourg','Q':'queenstown'})
print(titanic_df.head())

# data visualization 1
ax=sns.countplot(x='Pclass', hue='Survived', palette='Set1', data=titanic_df)
ax.set(title='passenger class VS survived', xlabel='passenger', ylabel='total')
print(pd.crosstab(titanic_df['Pclass'],titanic_df['Survived']))
plt.show()

# data visualization 2
bx=sns.countplot(x='Sex', hue='Survived',palette='Set2',data=titanic_df)
bx.set(title='gender VS survived', xlabel='sex', ylabel='survived')
plt.show()

# data visualization 3
cx=sns.countplot(x='Embarked', hue='Survived', palette='Set3', data=titanic_df)
cx.set(title='port VS survived',xlabel='port', ylabel='survived')
plt.show()

# data visualization 4
group=[0,18,35,60,120]
identity=['children', 'teens', 'adult', 'old']
titanic_df['Age_Cat']=pd.cut(titanic_df['Age'],group,labels=identity)

print(titanic_df.head())

dx=sns.countplot(x='Age_Cat', hue='Survived', palette='Set1', data=titanic_df)
dx.set(title='age category VS survived',xlabel='age category', ylabel='survived')
plt.show()
