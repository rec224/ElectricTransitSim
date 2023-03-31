import pandas as pd
import numpy
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

k=len(u_driver_ids)
class Driver:
    def __init__(self, op_id, num_drives, kwh) :
        self.op_id = op_id
        self.num_drives = num_drives
        self.kwh = kwh

driver_list = []
j=0
while j<k:
    n = driver_ids.count(u_driver_ids[j])
    driver_list.append(Driver(u_driver_ids[j], n, 0))
    #print('Driver_id %s w/ num_drives %s and kwh %d' % (u_driver_ids[j], n, 0))
    j=j+1   

kwh_sum_per_d=[]
z =0
while z<1:
    df2=dataframe1.loc[(dataframe1['op_id'] == u_driver_ids[z])]
    y = len(df2)
    print(y)
    z=z+1

#print(df2)