import pandas as pd
from scipy.stats import dgamma
import matplotlib.pyplot as plt
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
# here we are getting the kwh used from the actual vta data
i=0
kwh_list=[]
while(i<1374):
     cell3 = dataframe1.iloc[i]['kwh']
     kwh_list.append(cell3)
     i= i+1
# create dgamma distribution plot 
fig, ax = plt.subplots(1,1)
x = kwh_list
y= dgamma.pdf(kwh_list, 1.2217446905399747, 1.8631753076526738, 0.20790660522673732)
ax.plot(x, y, "ro")
plt.title('kwh dgamma plot')
plt.xlabel('List of kwh vals')
plt.ylabel('dgamma val')
plt.show()
