# -*- coding: utf-8 -*-
"""LAB-3__B21BB007.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hHyDMK8SAA9kxO44fYBIu-ax1zNpP21N

**QUE 1)**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns


data = pd.read_csv("diabetes.csv")
data

#Removing Null/NaN values.
dataDropNa = data.dropna(axis=0)
dataDropNa

data_fill = data.fillna(0)
data_fill

#Removing the Outliers using IQR
colum = np.array(data.columns)
new_data = pd.DataFrame(columns = data.columns)

for i in colum:
 
  percentile25 = data[i].quantile(0.25)
  percentile75 = data[i].quantile(0.75)
  iqr = percentile75 - percentile25
  upperlimit = percentile75 + 1.5*iqr
  lowerlimit = percentile25 - 1.5*iqr

  new_data[i] = data[(data[i] < upperlimit) & (data[i] > lowerlimit)][i] 


colum1 = np.array(new_data.columns)


for j in colum1:
  
  plt.figure()
  plt.subplot(2,2,1)
  sns.distplot(new_data[j])


  plt.subplot(2,2,2)
  sns.boxplot(new_data[j])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X = new_data.iloc[:,:8 ]
scaler.fit(X)
datascaled = scaler.transform(X)

datascaled

df_data = pd.DataFrame(datascaled)
df_data

df_data = df_data.dropna(axis=0)

new_data = new_data.dropna(axis=0)
new_data

df_data.columns = [ "Pregnancies" ,	"Glucose" ,	"BloodPressure"	,"SkinThickness",	"Insulin"	,"BMI",	"DiabetesPedigreeFunction",	"Age"	]
df_data

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
minmax.fit(X)
minmaxdata = minmax.transform(X)

minmaxdata[0:8]

#Spliting the dataset into training-validation-test splits
x = df_data.iloc[:,:].values
y = new_data["Outcome"].values

from sklearn.model_selection import train_test_split

x_main ,x_test , y_main , y_test  = train_test_split( x , y , test_size = 0.1 )

x_train , x_val , y_train , y_val = train_test_split(x_main , y_main , test_size = 0.2 )

"""**QUE 2**

Part A)
"""

#Training the model
x = df_data.iloc[:,:].values
y = new_data["Outcome"].values


from sklearn.model_selection import train_test_split

x_main ,x_test , y_main , y_test  = train_test_split( x , y , test_size = 0.2 )

x_train , x_val , y_train , y_val = train_test_split(x_main , y_main , test_size = 0.1 )

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 9)
knn.fit(x_train , y_train)

# from sklearn.linear_model import LogisticRegression
# lr = LogisticRegression()
# lr.fit(x_train , y_train)
# y_pred = lr.predict(x_test)
# accuracy_score(y_test , y_pred)

y_pred = knn.predict(x_test)

# Calculating Accuracy Score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy =", accuracy*100)

"""Part B )"""

import pandas as pd
  
import numpy as np
  
from sklearn.model_selection import train_test_split
  
from scipy.stats import mode
  
from sklearn.neighbors import KNeighborsClassifier
  
# K Nearest Neighbors Classification
  
class K_Nearest_Neighbors_Classifier() : 
      
    def __init__( self, K ) :
          
        self.K = K
          
    # Function to store training set
          
    def fit( self, X_train, Y_train ) :
          
        self.X_train = X_train
          
        self.Y_train = Y_train
          
        # no_of_training_examples, no_of_features
          
        self.m, self.n = X_train.shape
      
    # Function for prediction
          
    def predict( self, X_test ) :
          
        self.X_test = X_test
          
        # no_of_test_examples, no_of_features
          
        self.m_test, self.n = X_test.shape
          
        # initialize Y_predict
          
        Y_predict = np.zeros( self.m_test )
          
        for i in range( self.m_test ) :
              
            x = self.X_test[i]
              
            # find the K nearest neighbors from current test example
              
            neighbors = np.zeros( self.K )
              
            neighbors = self.find_neighbors( x )
              
            # most frequent class in K neighbors
              
            Y_predict[i] = mode( neighbors )[0][0]    
              
        return Y_predict
      
    # Function to find the K nearest neighbors to current test example
            
    def find_neighbors( self, x ) :
          
        # calculate all the euclidean distances between current 
        # test example x and training set X_train
          
        euclidean_distances = np.zeros( self.m )
          
        for i in range( self.m ) :
              
            d = self.euclidean( x, self.X_train[i] )
              
            euclidean_distances[i] = d
          
        # sort Y_train according to euclidean_distance_array and 
        # store into Y_train_sorted
          
        inds = euclidean_distances.argsort()
          
        Y_train_sorted = self.Y_train[inds]
          
        return Y_train_sorted[:self.K]
      
    # Function to calculate euclidean distance
              
    def euclidean( self, x, x_train ) :
          
        return np.sqrt( np.sum( np.square( x - x_train ) ) )
  
# Driver code
  
def main() :
      
    # Importing dataset
      
    df = pd.read_csv( "diabetes.csv" )
  
    X = df.iloc[:,:-1].values
  
    Y = df.iloc[:,-1:].values
      
    # Splitting dataset into train and test set
  
    X_train, X_test, Y_train, Y_test = train_test_split( 
      X, Y, test_size = 1/3, random_state = 0 )
      
    # Model training
      
    model = K_Nearest_Neighbors_Classifier( K = 3 )
      
    model.fit( X_train, Y_train )
      
    model1 = KNeighborsClassifier( n_neighbors = 3 )
      
    model1.fit( X_train, Y_train )
      
    # Prediction on test set
  
    Y_pred = model.predict( X_test )
      
    Y_pred1 = model1.predict( X_test )
      
    # measure performance
      
    correctly_classified = 0
      
    correctly_classified1 = 0
      
    # counter
      
    count = 0
      
    for count in range( np.size( Y_pred ) ) :
          
        if Y_test[count] == Y_pred[count] :
              
            correctly_classified = correctly_classified + 1
          
        if Y_test[count] == Y_pred1[count] :
              
            correctly_classified1 = correctly_classified1 + 1
              
        count = count + 1
          
    print( "Accuracy on test set by our model       :  ", ( 
      correctly_classified / count ) * 100 )
    print( "Accuracy on test set by sklearn model   :  ", ( 
      correctly_classified1 / count ) * 100 )
      
      
if __name__ == "__main__" : 
      
    main()

"""**QUE 3**

Part A)
"""

#Checking standard deviation
df_data.describe()

#Creating dataset using the features having maximum standard deviation 
data_3 = df_data[["Insulin" , "DiabetesPedigreeFunction" ]]
data_3["Outcome"] = new_data["Outcome"]
data_3 = data_3.dropna(axis=0)

"""Part B )"""

x = np.array(data_3["Insulin"]).reshape(-1 , 1)
y = np.array(data_3["Outcome"]).reshape(-1 , 1)

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier


x_main ,x_test , y_main , y_test  = train_test_split( x , y , test_size = 0.2 )

x_train , x_val , y_train , y_val = train_test_split(x_main , y_main , test_size = 0.1 )

# Discretize the features into n bins
from sklearn.preprocessing import KBinsDiscretizer
bin_disc = KBinsDiscretizer(n_bins= 10, encode='ordinal',strategy='uniform')
x_train_transformed = (bin_disc.fit_transform(x_train))

Knn = KNeighborsClassifier(n_neighbors = 10)
Knn.fit(x_train_transformed , y_train)

# Making Prediction
y_pred = Knn.predict(x_test)

# Calculating Accuracy Score
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy =", accuracy*100)

x = np.array(data_3["DiabetesPedigreeFunction"]).reshape(-1 , 1)
y = np.array(data_3["Outcome"]).reshape(-1 , 1)

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier


x_train ,x_test , y_train , y_test  = train_test_split( x , y , test_size = 0.2 ,random_state = 34 )

from sklearn.preprocessing import KBinsDiscretizer
bin_disc = KBinsDiscretizer(n_bins= 6, encode='ordinal',strategy='uniform')
x_train_transformed = (bin_disc.fit_transform(x_train))

y_pred = Knn.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_pred, y_test)
print("Accuracy =", accuracy*100)