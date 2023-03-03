import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('bigCSV.csv')
arr = df.to_numpy()

colorArr = ["red", "green", "blue", "orange", "purple", "skyblue", "hotpink", "teal", "lime", "navy", "goldenrod", "plum", "firebrick", "silver"]

for filter in range(0, 50, 1):
  for i in range (0, 157, 12):
      x = arr[:,i+2] #speed
      y = arr[:,i+4] #energy
      
      filter_arr = []
      for j in range(0,7368):
        if arr[j,i+11] < filter/100.0:
          filter_arr.append(False)
        else:
          filter_arr.append(True)

      newX = x[filter_arr]
      newY = y[filter_arr]
      
      l = str(2600+int(i/12))
      plt.scatter(newX,newY, 3, color=colorArr[int(i/12)], label = l)

  plt.xlabel("Average speed (mph)")
  plt.ylabel("Energy used (kWh)")
  plt.title("Energy (kWh) vs speed (mph) driving for at least " + str(filter) + " percent of the hour")
  # leg = plt.legend(loc ="upper right");
  filename = "animation_chartsv2/chart" + str(filter)
  plt.xlim(0,150)
  plt.ylim(0,65)
  plt.savefig(filename)
  plt.show()
