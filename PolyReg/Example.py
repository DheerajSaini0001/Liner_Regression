import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("polynomial_regression_dataset.csv")
print(pd.DataFrame(data))
x=data['X']
y=data['Y']
mymodel=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(min(x),max(x),100)
plt.scatter(x,y)
plt.plot(x,mymodel(myline))
plt.show()