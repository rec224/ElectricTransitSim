from matplotlib import patches
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from fitter import Fitter, get_distributions, get_common_distributions
dataframe1 = pd.read_excel('driver_data_points.xlsx')
#print(dataframe1)
#now we have to go through and group the data by driver ids
i =0
driver_ids =[]
while i<539:
    driver_ids.append(dataframe1.iloc[i]['op_id'])
    i=i+1
u_driver_ids = numpy.unique(driver_ids)
print(u_driver_ids)
kwh_avg_per_d=[]
z =0
while z<k:
    df2=dataframe1.loc[(dataframe1['op_id'] == u_driver_ids[z])]
    n = df2['kwh'].mean()
    kwh_avg_per_d.append(n)
    z=z+1
print(kwh_avg_per_d)
fig, ax = plt.subplots()
ax.plot(u_driver_ids, kwh_avg_per_d, 'ro')
plt.title('Mean kwh for each unique driver')
plt.xlabel('Driver')
plt.ylabel('kwh')
plt.show()
#print(df2)