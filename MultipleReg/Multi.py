import numpy as np
import pandas as pd
from sklearn import linear_model

data=pd.read_csv('car_data_200.csv')
x=data[['Volume','Weight']]
y=data['CO2']
reg=linear_model.LinearRegression()
reg.fit(x,y)
predictedCO2=reg.predict([[4.3,900]])
print(predictedCO2)