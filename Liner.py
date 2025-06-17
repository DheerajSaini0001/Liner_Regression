import numpy as np
from scipy import stats as st
from matplotlib import pyplot as plt
import pandas as pd
# Car=pd.read_csv('car_speed_age.csv')
# pd.DataFrame(Car)
# print(Car.head())
age=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
speed=np.array([180,135,172,128,125,110,158,155,152,90,147,145,70,140,138])

# x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
# y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

slope, interception, r ,p ,Std_error=st.linregress(age,speed)
def fun(age):
        return slope*age + interception
mymodel=list(map(fun,age))
plt.scatter(age,speed)
plt.plot(age,mymodel)
plt.xlabel("Age of Car")
plt.ylabel("Speed of Car")
plt.title("Graph Showing the RelationShip Between Speed and Age of Car")
'''
slope1, interception1, r1 ,p1 ,Std_error1=st.linregress(x,y)
def func1(x):
        return slope1*x+interception1
mymodel1=list(map(func1,x))
plt.scatter(x,y)
plt.plot(x,mymodel1)
'''
print("Relationship Between age ang Speed of Car =",r)
# plt.legend()
plt.show()
