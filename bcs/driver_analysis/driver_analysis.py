import pandas as pd
import numpy
import matplotlib.pyplot as plt
dataframe1 = pd.read_excel('driver_data_points.xlsx')
#now we have to go through and group the data by driver ids
i =0
driver_ids =[]
while i<539:
    driver_ids.append(dataframe1.iloc[i]['op_id'])
    i=i+1
# now we want to pull out the unique driver ids so we can search through the data frame
u_driver_ids = numpy.unique(driver_ids)
print(u_driver_ids)
kwh_avg_per_d=[]
z =0
# get the mean kwh for each unique driver by making a new dataframe for each driver and then summing the'kwh' column
while z<136:
    df2=dataframe1.loc[(dataframe1['op_id'] == u_driver_ids[z])]
    n = df2['kwh'].mean()
    kwh_avg_per_d.append(n)
    z=z+1
print(kwh_avg_per_d)
# plot the driver against there avg kwh 
# I ended up putting kwh on the x axis so that an analytical tool like a box and wiskers plot could be easily visualized 
# to determine which drivers are outliers. 
fig, ax = plt.subplots()
ax.plot(kwh_avg_per_d, u_driver_ids, 'ro')
plt.title('Mean kwh for each unique driver')
plt.xlabel('kwh')
plt.ylabel('Driver')
plt.show()