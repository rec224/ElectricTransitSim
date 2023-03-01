#most helpful example for the actual simulation
#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
#import these to create a normal distribution
from numpy.random import normal
#display the histogram of the distribution
import matplotlib.pyplot as plt
import time
#routes = [1,2,3]
#r_times = [20, 25, 30]
 
# is sample size based on number of buses or number of routes or bus drivers etc.?
#mean = 2
#std = 0.005
#energy_cons_dst = normal(2, 0.005, 50)
# ^ creates normal dist w median 2, std dev 0.005, and sample size 50
# create a histrogram to show the normal distribution (10 bins)
#count, bins, ignored = plt.hist(energy_cons_dst, 10)
#plt.show()
#try treating the buses as an object with own state of charge etc. 
#def bus(env, name, battery):
    # battery will drain -- find out a way for it to vary
    # select random number of miles from range of options
    #miles = random.randint(50, 150)
    # select random value from the probability distribution
    # needs some sort of division or percentage function, 
    # otherwise, battery percentage ends up negative
    #energy_cons_val = random.normalvariate(mean, std)
    #calculate the random amount of energy used 
    #energy is in kW*hrs
    #battery is 440
    #energy = miles * energy_cons_val
    #gives percetage out of 440
    #battery = ((battery - energy)/440) *100
    #print('Bus %d returning with %d percent battery' %(i , battery))
#miles = random.randint(50, 150)
class Bus:
    def __init__(self, charge, r_dist):
        self.charge = charge
        self.r_dist = r_dist

busList = []
i = 0
mean = 2
std = 0.005
energy_cons_dst = normal(2, 0.005, 50)
# ^ creates normal dist w median 2, std dev 0.005, and sample size 50
# create a histrogram to show the normal distribution (10 bins)
count, bins, ignored = plt.hist(energy_cons_dst, 10)
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
    busList.append(Bus(battery,miles))
    i=i+1

env = simpy.Environment()
# can ignore anything below here, this stuff will be useful later: 


# capacity limites the number of charging spots to 6 -- how many are there actually
# resource limits are not important right now
# bcs = simpy.Resource(env, capacity=6)
# accurate bus numbers

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
    #the duration of the drive will vary, lets call average of 120 minutes and std of 20 minutes
    drive_dur = random.normalvariate(120, 20)
    #calculate return time
    return_time = drive_dur + scheduled_start
    return_hr = return_time/60
    return_12 = "am"
    if return_hr > 12 and return_hr <24:
         return_12 = "pm"
    if(return_hr ==0):
            return_hr = 12
    return_min = return_time%60
    if return_hr > 12:
         return_hr = return_hr -12
    freturn_time = "%02d:%02d" % (return_hr, return_min) 
    freturn_time = freturn_time + return_12
    print('Bus %d returning at time %s' % (i+1, freturn_time))
    bat = busList[i].charge
    mil = busList[i].r_dist
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
    print('Expected return %s' % efreturn_time)
    #increment the scheduled start time for the next bus
    scheduled_start = scheduled_start + 120
    print('\n')


env.run()