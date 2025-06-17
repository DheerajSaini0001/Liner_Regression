import numpy as np
from scipy import stats as st
from matplotlib import pyplot as plt
import pandas as pd
# Car=pd.read_csv('car_speed_age.csv')
# pd.DataFrame(Car)
# print(Car.head())
age=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
speed=np.array([180,135,172,128,125,110,158,155,152,90,147,145,70,140,138])

slope, interception, r ,p ,Std_error=st.linregress(age,speed)

def fun(age):
    return slope*age + interception
mymodel=list(map(fun,age))
plt.scatter(age,speed)
plt.plot(age,mymodel)
plt.show()
