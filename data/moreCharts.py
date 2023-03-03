import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datafm = pd.read_csv("../vta energy consumption data.csv")
vta_arr = datafm.to_numpy() 
datafm

efficency = vta_arr[:, 5]
miles = vta_arr[:, 7]
total = efficency * miles

dfm = pd.read_csv("../ReportsTimDis.csv")
vir_arr = dfm.to_numpy() 

for i in range (0, 28, 2):
    y = vir_arr[:,i+1] #energy used
    x = vir_arr[:,i+2] #distance
#     l = str(2600+int(i/12));
    
#     filter_arr = []
#     for j in range(0, len(x)):
#         if(x[j]>100):
#             filter_arr.append(False)
#         else:
#             filter_arr.append(True)

#     newX = x[filter_arr]
#     newY = y[filter_arr]
    if(i == 0 ):
        plt.scatter(x,y, 1, color='r', label = "Viriciti")
        plt.scatter(miles, total,2,color = 'b', label = "VTA");
    else:
        plt.scatter(x,y, 1, color='r')
        plt.scatter(miles, total,2,color = 'b');


plt.xlabel("Distance driven (miles)")
plt.ylabel("Energy used (kWh)")
leg = plt.legend(loc ="upper right");
plt.show()