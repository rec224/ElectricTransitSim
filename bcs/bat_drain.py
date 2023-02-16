#most helpful example for the actual simulation
#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
#import these to create a normal distribution
import numpy
from numpy.random import normal
#display the histogram of the distribution
import matplotlib.pyplot as plt
routes = [1,2,3]
r_times = [20, 25, 30]
battery = 100
# what do we want the standard deviation of the distribution to be her
# use scipy.stats.norm instead? 
# is sample size based on number of buses or number of routes or bus drivers etc.?
mean = 2
std = 0.005
energy_cons_dst = normal(2, 0.005, 50)
# ^ creates normal dist w median 2, std dev 0.005, and sample size 10
# create a histrogram to show the normal distribution
count, bins, ignored = plt.hist(energy_cons_dst, 10)
plt.show()

# select random number of miles from range of options
miles = random.randint(50, 150)


# select random value from the probability distribution
# needs some sort of division or percentage function, 
# otherwise, battery percentage ends up negative
energy_cons_val = random.normalvariate(mean, std)/3
#calculate the random amount of energy used 
energy = miles * energy_cons_val
def bus(env, name, battery):
    # battery will drain -- find out a way for it to vary
    battery = battery - energy
    print('Bus on route  returning with %d percent battery' %battery)
env = simpy.Environment()
# capacity limites the number of charging spots to 6 -- how many are there actually
# resource limits are not important right now
# bcs = simpy.Resource(env, capacity=6)
# accurate bus numbers
for i in range(0,5):
    #lets say buses have to charge for 3 hrs
    #want battery recorded too? 
    bus(env, 'Bus %d' % i, battery)



env.run()