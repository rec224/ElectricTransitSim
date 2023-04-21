import pandas as pd
import matplotlib.pyplot as plt
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
# here we are getting the kwh used from the actual vta data
i=0
kwh_list=[]
while(i<1374):
     cell3 = dataframe1.iloc[i]['kwh']
     kwh_list.append(cell3)
     i= i+1
#create a histogram showing the kwh list so that we can compare with the dgamma distribution
fig, ax = plt.subplots(1,1)
x = kwh_list
# changing the number of bns to 100 better shows the dgamma distribution
n_bins = 100
ax.hist(x, n_bins)
plt.title('kwh histogram')
plt.xlabel('List of kwh vals')
plt.ylabel('frequency')
plt.show()
