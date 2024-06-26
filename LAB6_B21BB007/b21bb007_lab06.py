# -*- coding: utf-8 -*-
"""B21BB007_Lab06

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1W9DzfgEZWKncDuYpQccKutQ2UyNujbEs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans

data = pd.read_csv("wine.data")

data.columns = ["Class" , 'Alcohol' , "Malic acid" , "Ash" , ' Alcalinity of ash' , ' Magnesium' , 'Total phenols' , ' Flavanoids', 'Nonflavanoid phenols' , 'Proanthocyanins' , 'Color intensity', 'Hue' , 'OD280/OD315 of diluted wines' , 'Proline']

df_data = data.dropna(axis=0)

df_data

s = df_data.iloc[: , 0].values
s

x = df_data.iloc[ : , 1:14].values

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
minmax.fit(x)
x = minmax.transform(x)

x

sns.set_style("whitegrid")
sns.pairplot(df_data,size=3);
plt.show()

sns.set_style("whitegrid")
sns.pairplot(df_data,hue = "Class" ,size=3);
plt.show()

true_labels = s

true_labels_list = []

for i in true_labels:
  if i== 1:
    true_labels_list.append(1)
  elif i== 2:
    true_labels_list.append(0)
  else:
    true_labels_list.append(2)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 600, n_init = 140, random_state = 0)
y_kmeans = kmeans.fit_predict(x)

print("True Class Labels :- ")
print(true_labels_list)

print("Predicted Class labels :- ")
print(kmeans.labels_)

plt.figure(figsize=(10,5))
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'red', label = '1')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'orange', label = '2')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'green', label = '3')

#Plotting the centroids of the cluster
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'black', label = 'Centroids')

plt.legend()

