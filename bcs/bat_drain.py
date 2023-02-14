#most helpful example for the actual simulation
#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
routes = [1,2,3]
r_times = [20, 25, 30]
def bus(env, name, battery):
    route = random.randint(1,3)
    r_time = r_times[route]
    # battery will drain -- find out a way for it to vary
    battery = battery - r_time
    #request charging spot
    print('%s arriving at %d' % (name, env.now))
    with bcs.request() as req:
        yield req

        #charge battery
        print('%s starting to charge at %s' % (name, env.now))
        yield env.timeout(charge_duration)
        battery = 100
        print('%s leaving the bcs at %s' % (name, env.now))

env = simpy.Environment()
# capacity limites the number of charging spots to 6 -- how many are there actually
# resource limits are not important right now
bcs = simpy.Resource(env, capacity=6)
# accurate bus numbers
for i in range(0,5):
    #lets say buses have to charge for 3 hrs
    #want battery recorded too? 
    env.process(bus(env, 'Bus %d' % i, bcs, i, 2, i+5))

env.run()