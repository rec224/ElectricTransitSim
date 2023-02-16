import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bigCSV.csv')

arr = df.to_numpy()
# print(arr)
# print(arr[:,2])

colorArr = ["red", "green", "blue", "orange", "purple", "skyblue", "hotpink", "teal", "lime", "navy", "goldenrod", "plum", "firebrick", "silver"]
for i in range (0, 157, 12):
    x = arr[:,i+2]
    y = arr[:,i+8]
    
    filter_arr = []
    for element in x:
      if element < 60:
        filter_arr.append(True)
      else:
        filter_arr.append(False)

    newX = x[filter_arr]
    newY = y[filter_arr]
    
    l = str(2600+int(i/12));
    plt.scatter(newX,newY, 3, color=colorArr[int(i/12)], label = l)

plt.xlabel("Average speed")
plt.ylabel("Energy regenerated driven")
leg = plt.legend(loc ="upper right")

plt.show()

for i in range (0, 157, 12):
    x = arr[:,i+11]
    y = arr[:,i+3]
    
    l = str(2600+int(i/12));
    plt.scatter(x,y, 3, color=colorArr[int(i/12)], label = l)

plt.xlabel("Time driving")
plt.ylabel("Energy driven")
leg = plt.legend(loc ="upper right")

plt.show()

for i in range (0, 157, 12):
    x = arr[:,i+11]
    y = arr[:,i+5]
    
    l = str(2600+int(i/12));
    plt.scatter(x,y, 3, color=colorArr[int(i/12)], label = l)

plt.xlabel("Time driving")
plt.ylabel("Energy idled")
leg = plt.legend(loc ="upper right")

plt.show()