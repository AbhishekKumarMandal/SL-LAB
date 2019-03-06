import pandas as pd
#from pandas import Series,DataFrame
iris_df = pd.read_csv("iris.csv")
print("printing iris data frame completely")
print(iris_df)
print("printing info")
iris_df.info()
print("printing using dataframe functions")
print(iris_df[["Class", "Sepal_Length"]].groupby(['Class'], as_index=True).mean())
a = iris_df['Sepal_Length'].max()
print("The maximum sepal length is :",round(iris_df['Sepal_Length'].max(),2))
print()
print("Class of max lenght sepal is ")
print(iris_df.loc[iris_df['Sepal_Length'] == a])