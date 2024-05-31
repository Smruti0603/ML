# -*- coding: utf-8 -*-
"""LAB2 _B21BB007.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q_FN3UwlNyl2PPLc3pe7Z64gOWtF4riB

**Que 1 :**
"""

import pandas as pd
import numpy as np
data = pd.read_csv("job_salaries.csv")

#determine the columns with missing rows 

data.loc[:, data.isnull().any()].columns

print(data["salary"].dtype)
print(data["job_title"].dtype)
print(data["company_size"].dtype)

"""**QUE 2:**"""

data.columns

data.info()

dataDropNa = data.dropna(axis=0)
dataDropNa

dataDropNa.info()

data = data.drop([ "Unnamed: 0"] , axis=1)
data.info()

data_fill = data.fillna(0)
data_fill

data.isnull()

"""**QUE 5:**"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X = data.iloc[:,[4,6] ]
scaler.fit(X)
datascaled = scaler.transform(X)

datascaled

df_data = pd.DataFrame(datascaled)

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
minmax.fit(X)
minmaxdata = minmax.transform(X)

minmaxdata[5:7,]

data_fill.head()

"""**QUE 6: b)**"""

x = data_fill.iloc[:,1:].values
y = data_fill.iloc[:,7].values

from sklearn.model_selection import train_test_split



x_main ,x_test , y_main , y_test  = train_test_split( x , y , test_size = 0.2 )

x_train , x_val , y_train , y_val = train_test_split(x_main , y_main , test_size = 0.1 )

"""**a)**

"""

train, validation, test = np.split(data.sample(frac=1), [int(.7*len(data)), int(.9*len(data))])

"""**Que 4:**"""

dum_df = pd.get_dummies( data, drop_first=True)
dum_df

#Nominal Encoding
from sklearn.model_selection import train_test_split

x_train ,x_test , y_train , y_test  = train_test_split( data.iloc[:,:5] , data.iloc[: ,7] , test_size = 0.3 , random_state = 2021)

x_train

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop = "first" , sparse = False)

x_train_new = ohe.fit_transform(x_train[["job_title"]])
x_test_new = ohe.fit_transform(x_test[["job_title"]] )

np.hstack((x_train[["job_title"]].values , x_train_new))

#ordinal Encoding
data1 = dataDropNa.iloc[: ,-1 ]

data1.head

from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['L' , 'M' , 'S']])

oe.fit(np.array(data1).reshape(-1 ,1))

x = oe.transform(np.array(data1).reshape(-1,1))
x

data1

"""**QUE 3:**"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16,5))
plt.subplot(1,2,1)
sns.distplot(data["salary_in_usd"])
plt.show()

data["salary_in_usd"].skew()

data["salary_in_usd"].describe()

sns.boxplot(data["salary_in_usd"])

percentile25 = data["salary_in_usd"].quantile(0.25)
percentile75 = data["salary_in_usd"].quantile(0.75)

iqr = percentile75 - percentile25
iqr

upperlimit = percentile75 + 1.5*iqr
lowerlimit = percentile25 - 1.5*iqr

print(upperlimit , lowerlimit)

data[data["salary_in_usd"] > upperlimit]

data[data["salary_in_usd"] < lowerlimit]

new_data = data[data["salary_in_usd"] < upperlimit]
new_data

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline



plt.subplot(2,2,1)
sns.distplot(data['salary_in_usd'])


plt.subplot(2,2,2)
sns.boxplot(data['salary_in_usd'])

plt.subplot(2,2,3)
sns.distplot(new_data['salary_in_usd'])


plt.subplot(2,2,4)
sns.boxplot(new_data["salary_in_usd"])




plt.show()

