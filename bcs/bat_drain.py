#want the simulation to predict battery charge based on what a bus leaves with
#and given a particular route
import simpy
import random
import pandas as pd
from charge_time import charge_time
#import to use dgamma distribution
from scipy.stats import dgamma, laplace_asymmetric
#display the histogram of the distribution
import matplotlib.pyplot as plt
import numpy
import matplotlib.patches as mpatches 
#import Nick's code for assigning routes
from helpers import initRoutes
class Bus:
    def __init__(self, charge, route_len, driver, route, s_d_time, e_d_time, s_c_time, e_c_time, s_charge, e_charge):
        self.charge = charge
        self.route_len = route_len
        self.driver = driver
        self.route = route
        self.s_d_time = s_d_time
        self.e_d_time = e_d_time
        self.s_c_time = s_c_time
        self.e_c_time = e_c_time
        self.s_charge = s_charge
        self.e_charge = e_charge

busList = []
opt_bus_list=[]
i = 0
#Now we'll create the dgamma distribution and use that to initialize buses
kwh_df = pd.read_excel('clean_drive_data.xlsx')
# here we are getting the miles traveled and the percentage battery used from the actual vta data
j=0 
kwh_list=[]
miles_list=[]
while(j<1374):
     cell1 = kwh_df.iloc[j]['miles_travelled']
     miles_list.append(cell1)
     cell3 = kwh_df.iloc[j]['kwh']
     kwh_list.append(cell3)
     j= j+1
a= 1.2217446905399747
loc =1.863175307652673
scale =0.20790660522673732
kwh_cons_dist = dgamma.pdf(kwh_list, a, loc, scale)
#miles_trav_dist = laplace_asymmetric.pdf(miles_list)
#plt.show()
#use the data to make a list of the possible routes 

route_list = pd.read_excel('clean_routes.xlsx')
driver_df = pd.read_excel('driver_data_points.xlsx')
k =len(route_list) -1
#now we have to go through and group the data by driver ids
w =0
driver_ids =[]
while w<539:
    driver_ids.append(driver_df.iloc[w]['op_id'])
    w=w+1
u_driver_ids = numpy.unique(driver_ids)
#get the arrays created in charge_time
charging = pd.read_excel('charge_time.xlsx')
charging_t =[]
charging_b=[]
p=0
while (p<len(charging)):
     charging_t.append(charging.iloc[p]['change in hrs'])
     charging_b.append(charging.iloc[p]['change in charge'])
     p=p+1
while(i<11):
    battery = 440
    kwh_cons_val = dgamma.rvs(a, loc, scale, 1)
    miles = laplace_asymmetric.rvs(0.5656655470214752, 49.999996346657085, 17.774262322316076, 1)
    #calculate the random amount of energy used 
    #energy is in kW*hrs
    #battery is 440
    #energy = miles * energy_cons_val
    b= random.randint(0, len(charging)-1)
    s_charge_list, e_charge_list, s_time_list, ct_time_list=charge_time()
    v = random.randint(0, k)
    s_d_time =route_list.iloc[v]['s_mins']
    e_d_time =route_list.iloc[v]['e_mins']
    convert_mins = s_d_time
    hours = convert_mins/60
    convert_mins = convert_mins%60
    d_s_t = '%02d:%02d' %(hours, convert_mins)
    conver_mins = e_d_time
    hours = conver_mins/60
    conver_mins = conver_mins%60
    d_e_t = '%02d:%02d' %(hours, conver_mins)
    s_c_t= d_e_t
    e_mins = e_d_time + 60*charging_t[b]
    conv_min = e_mins%60
    conv_hrs = e_mins/60
    if(conv_hrs >24):
         conv_hrs = conv_hrs -24
    e_c_t = '%02d:%02d' %(conv_hrs, conv_min)
    energy = miles*kwh_cons_val
    #gives percetage out of 440
    battery = ((battery - energy)/440) *100
    s_charge = battery
    e_charge = s_charge + charging_b[b]
    if(e_charge > 100):
         e_charge=100
    hrs = (e_charge -s_charge - 5.1166)/8.6519
    d_id = random.randint(0, len(u_driver_ids)-1)
    driver = u_driver_ids[d_id]
    index = random.randint(0, 281)
    route = route_list.iloc[index]['routeNum']
    busList.append(Bus(battery, miles, driver, route, d_s_t, d_e_t, s_c_t, e_c_t, s_charge, e_charge))
    print('Battery: %d\nmiles: %s\ndriver: %s\nroute: %d\nstart drive time: %s\nend drive time: %s\nstart charge time: %s\nend charge time: %s\nstart charging: %d\nend charging: %d\n' % (battery, miles, driver, route, d_s_t, d_e_t, s_c_t, e_c_t, s_charge, e_charge))
    #print(hrs*60)
    #print (60*charging_t[b])
    if(hrs*60 < 60*charging_t[b]):
          conv_min = (hrs/1)*60 + s_d_time + (hrs%1)*60
          conv_hrs = conv_min/60
          if(conv_hrs >24):
              conv_hrs = conv_hrs -24
          e_c_t = '%02d:%02d' %(conv_hrs, conv_min)
          opt_bus_list.append(Bus(battery, miles, driver, route, d_s_t, d_e_t, s_c_t, e_c_t, s_charge, e_charge))
    else:
          opt_bus_list.append(Bus(battery, miles, driver, route, d_s_t, d_e_t, s_c_t, e_c_t, s_charge, e_charge))
    i=i+1

# here we want to check the data from the VTA file
# going to import the battery and mileage , multiply, use that to create data!
#f = Fitter(energy_cons_dst)
#f.fit()
#f.summary()
env = simpy.Environment()
'''start_list = []
ret_list = []
eret_list =[]
list_pairs = []
raw_ret_list=[]
raw_eret_list=[]
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
    raw_ret_list.append(return_time)
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
    raw_eret_list.append(ereturn_time)
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
    print('\n')'''
plt.style.use('_mpl-gallery')
charge_list =[]
opt_chg_time =[]
nonopt_chg_time=[]

for i in range(0,10):
     dcharge = busList[i].e_charge - busList[i].s_charge
     charge_list.append(dcharge)
     t_charge = opt_bus_list[i].e_c_time
     t_chargei = opt_bus_list[i].s_c_time
     tm = t_charge.split(":")
     tmi = t_chargei.split(":")
     tcharge = (int(tm[0])-int(tmi[0]))
     if(tcharge<0):
          tcharge = tcharge +24
     tcharge = tcharge*60
     tmin = int(tm[1]) - int(tmi[1])
     if(tmin <0):
          tmin = 60-tmin
          tcharge = tcharge-60
     tcharge = tcharge + tmin
     opt_chg_time.append(tcharge)

     nont_chg = busList[i].e_c_time
     nont_chgi = busList[i].s_c_time
     otm = (nont_chg.split(":"))
     otmi = (nont_chgi.split(":"))
     otcharge = (int(otm[0])-int(otmi[0]))
     if(otcharge<0):
          otcharge = 24+ otcharge
     otcharge = otcharge*60
     otmin = int(otm[1]) - int(otmi[1])
     if(otmin <0):
          otmin = 60-otmin
          otcharge = otcharge-60
     otcharge = otcharge + otmin
     nonopt_chg_time.append(otcharge)

# make the data
x = charge_list 
y1 = opt_chg_time 
y2 = nonopt_chg_time
print(y1)
print(y2)
#print(y2)
vals =  ['Optimal', 'Nonoptimal']
# plot
fig, ax = plt.subplots()
red_patch = mpatches.Patch(color='red', label='Optimal End Charge')
green_patch = mpatches.Patch(color ='green', label = 'Nonoptimal End Charge')
ax.legend(handles=[red_patch, green_patch])
plt.plot(x, y1, 'ro', x, y2, 'go')
#plt.plot(x, y2, 'go', label ='nonoptimal charge')
plt.title('Comparing Time Charging to Time Needed')
plt.xlabel('Inital Battery %')
plt.ylabel('Change in Time (mins)')
#plt.scatter(*zip(*list_pairs))
plt.show()

env.run()