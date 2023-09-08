# import python libraries

import numpy as np 
import pandas as pd 
#import matplotlib.pyplot as plt # visualizing data
# import seaborn as sns

# import csv file
df = pd.read_csv('https://raw.githubusercontent.com/mohammadrakibulhasan/eda1/main/Diwali%20Sales%20Data.csv', encoding= 'unicode_escape')
df.shape
df.head()
df.info()
#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
#check for null values
pd.isnull(df).sum()
# drop null values
df.dropna(inplace=True)
# change data type
df['Amount'] = df['Amount'].astype('int')
df['Amount'].dtypes
df.columns
#rename column
df.rename(columns= {'Marital_Status':'Shaadi'})
# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
df.describe()
# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()

# plotting a bar chart for Gender and it's count

# ax = sns.countplot(x = 'Gender',data = df)

# for bars in ax.containers:
#     ax.bar_label(bars)
