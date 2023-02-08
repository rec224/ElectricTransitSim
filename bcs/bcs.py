#most helpful example for the actual simulation
import simpy
def bus(env, name, bcs, route_time, charge_duration, battery):
    #simulate driving to the BCS
    yield env.timeout(route_time)
    # battery will drain -- find out a way for it to vary
    battery = battery - 15
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
bcs = simpy.Resource(env, capacity=6)
# accurate bus numbers
for i in range(2600,2614):
    #lets say buses have to charge for 3 hrs
    #want battery recorded too? 
    env.process(bus(env, 'Bus %d' % i, bcs, (i-2600)*2, 3, 83))

env.run()