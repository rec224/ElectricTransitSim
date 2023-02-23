#most helpful example for the actual simulation
#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
#import these to create a normal distribution
from numpy.random import normal
#display the histogram of the distribution
import matplotlib.pyplot as plt
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

#running the file for 5 buses (five times)
#schedule for the buses starts at time 0, expected route duration is 2hrs (120 min)
scheduled_start = 0
for i in range(0,10): 
    #bus leaves at a cheduled time (everry 120 minutes)
    print('Bus %d leaving at time %d' % (i+1, scheduled_start))
    #the duration of the drive will vary, lets call average of 120 minutes and std of 45 minutes
    drive_dur = random.normalvariate(120, 45)
    #calculate return time
    print('Bus %d returning at time %d' % (i+1, scheduled_start + drive_dur))
    bat = busList[i].charge
    mil = busList[i].r_dist
    print('Bus %d returning with %d percent charge after %d miles'% (i+1, bat, mil))
    print('Expected return %d' %(scheduled_start + 120))
    #increment the scheduled start time for the next bus
    scheduled_start = scheduled_start + 120
    print('\n')


env.run()