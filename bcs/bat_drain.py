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
#what do we want the standard deviation of the distribution to be her
# use scipy.stats.norm instead? 
# is sample size based on number of buses or number of routes or bus drivers etc.?
energy_cons_dst = normal(2, 0.005, 10)
# ^ creates normal dist w median 2, std dev 0.005, and sample size 10
count, bins, ignored = plt.hist(energy_cons_dst, 1)
plt.show()
def bus(env, name, battery):
    route = random.randint(1,3)
    r_time = r_times[route-1]
    # battery will drain -- find out a way for it to vary
    battery = battery - r_time
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