#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
import pandas as pd
#import these to create a normal distribution
from numpy.random import normal
#display the histogram of the distribution
import matplotlib.pyplot as plt
import numpy
import matplotlib.patches as mpatches 
from fitter import Fitter
class Bus:
    def __init__(self, charge, route_len, driver, route, s_time, e_time):
        self.charge = charge
        self.route_len = route_len
        self.driver = driver
        self.route = route
        self.s_time = s_time
        self.e_time = e_time

busList = []
i = 0
mean = 2
std = 0.005
energy_cons_dst = normal(2, 0.005, 50)
# ^ creates normal dist w median 2, std dev 0.005, and sample size 50
# create a histrogram to show the normal distribution (10 bins)
# count, bins, ignored = plt.hist(energy_cons_dst, 10)
plt.show()
while(i<11):
    battery = 440
    miles = random.randint(50, 150)
    energy_cons_val = random.normalvariate(mean, std)
    #calculate the random amount of energy used 
    #energy is in kW*hrs
    #battery is 440
    energy = miles * energy_cons_val
    #gives percetage out of 440
    battery = ((battery - energy)/440) *100
    driver = "Driver Name"
    route = random.randint(1,10)
    s_time = 0
    e_time = 120
    busList.append(Bus(battery,miles, driver, route, s_time, e_time))
    i=i+1
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
print(dataframe1)
# here we are getting the miles traveled and the percentage battery used from the actual vta data
i=0
mile_list = []
perc_used_list =[]
while(i<1374):
     cell1 = dataframe1.iloc[i]['miles_travelled']
     mile_list.append(cell1)
     cell2 = dataframe1.iloc[i]['percent_used']
     perc_used_list.append(cell2)
     i= i+1
print(mile_list)
print(perc_used_list)
# here we want to check the data from the VTA file
# going to import the battery and mileage , multiply, use that to create data!
#f = Fitter(energy_cons_dst)
#f.fit()
#f.summary()
env = simpy.Environment()
start_list = []
ret_list = []
eret_list =[]
list_pairs = []
#schedule for the buses starts at time 0, expected route duration is 2hrs (120 min)
scheduled_start = 240
for i in range(0,10): 
    #bus leaves at a cheduled time (everry 120 minutes)
    leave_hr = scheduled_start/60
    leave_12 = "pm"
    if leave_hr < 12:
         leave_12 = "am"
    if(leave_hr ==0):
            leave_hr = 12
    leave_min = scheduled_start%60
    if leave_hr > 12:
         leave_hr = leave_hr -12
    leave_time = "%02d:%02d" % (leave_hr, leave_min) 
    leave_time = leave_time + leave_12
    print('Bus %d leaving at time %s' % (i+1, leave_time))
    start_list.append(leave_time)
    #the duration of the drive will vary, lets call average of 120 minutes and std of 20 minutes
    drive_dur = random.normalvariate(120, 20)
    #calculate return time
    return_time = drive_dur + scheduled_start
    return_hr = return_time/60
    return_12 = "am"
    if return_hr > 12 and return_hr <24:
         return_12 = "pm"
    return_min = return_time%60
    if return_hr > 13:
         return_hr = return_hr -12
    if return_hr == 0:
         return_hr = return_hr + 12
    ## i have a bug in here going from am to pm 
    freturn_time = "%02d:%02d" % (return_hr, return_min) 
    freturn_time = freturn_time + return_12
    print('Bus %d returning at time %s' % (i+1, freturn_time))
    ret_list.append(freturn_time)
    bat = busList[i].charge
    mil = busList[i].route_len
    print('Bus %d returning with %d percent charge after %d miles'% (i+1, bat, mil))
    #est ret time
    ereturn_time = scheduled_start +120
    ereturn_hr = ereturn_time/60
    ereturn_12 = "pm"
    if ereturn_hr < 12:
         ereturn_12 = "am"
    if(ereturn_hr ==0):
            ereturn_hr = 12
    ereturn_min = ereturn_time%60
    if ereturn_hr > 12:
        ereturn_hr = ereturn_hr -12
        if ereturn_hr == 12:
            ereturn_12 = "am"
    
    efreturn_time = "%02d:%02d" % (ereturn_hr, ereturn_min) 
    efreturn_time = efreturn_time + ereturn_12
    list_pairs.append((scheduled_start, freturn_time))
    list_pairs.append((scheduled_start, efreturn_time))
    print('Expected return %s' % efreturn_time)
    eret_list.append(efreturn_time)
    #increment the scheduled start time for the next bus
    scheduled_start = scheduled_start + 120
    print('\n')
plt.style.use('_mpl-gallery')

# make the data
x = start_list
y1 = ret_list
y2 = eret_list
vals =  ['Estimated', 'Actual']
# plot
fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label='Estimated Return Time')
green_patch = mpatches.Patch(color ='green', label = 'Actual Return Time')
ax.legend(handles=[red_patch, green_patch])
ax.plot(x, y1, 'go')
ax.plot(x, y2, 'ro')
plt.title('Difference Between Expected Return and Actual Return')
plt.xlabel('Scheduled Start Time')
plt.ylabel('Return Time')
#plt.scatter(*zip(*list_pairs))
plt.show()

env.run()