import pandas as pd
#from fitter import Fitter, get_distributions
import matplotlib.pyplot as plt
#install seaborn
import seaborn as sns
import openpyxl
#unplug must be greater than plug in
#does not deal with changing years
def time_dif(plug_inm,plug_ind, plug_int, unplugm, unplugd, unplugt):
    dayDif =0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #deal with days going across months
    m1= int(plug_inm)
    m2 = int(unplugm)
    if(m2 > m1):
        tot_days = days[plug_inm]
        day_num1= tot_days - int(plug_ind)
        dayDif= day_num1 +int(unplugd)
    else:
        dayDif = unplugd-plug_ind
    plug_t = str(plug_int).split(':')
    unplug_t = str(unplugt).split(':')
    plug_hr = int(plug_t[0])
    plug_min = int(plug_t[1])
    unplug_hr = int(unplug_t[0])
    unplug_min = int(unplug_t[1])
    #get time stamp from first day
    start_mins = plug_hr*60 + plug_min
    #difference in hours
    hr_dif = unplug_hr - plug_hr
    if(hr_dif < 0):
        hr_dif = 24 + hr_dif
        dayDif = dayDif -1
    min_dif = unplug_min - plug_min
    if(min_dif < 0):
        min_dif = 60 +min_dif
        hr_dif = hr_dif -1
    total_mins = min_dif + 60*hr_dif + 24*60*dayDif
    return start_mins, total_mins
def charge_time():
    #read the excel file with the charging data
    charge_data = pd.read_excel('chargepoint_merged.xlsx')
    #print(charge_data)
    k =len(charge_data) -1
    s_charge_list =[]
    e_charge_list =[]
    s_time_list=[]
    ct_time_list =[]
    delta_time_list=[]
    delta_charge_list=[]
    while k>0:
        plug_inm = charge_data.iloc[k]['Session plug-inm']
        plug_ind = charge_data.iloc[k]['Session plug-ind']
        plug_iny = charge_data.iloc[k]['Session plug-iny']
        plug_int = charge_data.iloc[k]['Session plug-int']
        unplugm = charge_data.iloc[k]['Session unplugm']
        unplugd = charge_data.iloc[k]['Session unplugd']
        unplugy = charge_data.iloc[k]['Session unplugy']
        unplugt = charge_data.iloc[k]['Session unplugt']
        start_min, mins_charging = time_dif(plug_inm,plug_ind, plug_int, unplugm, unplugd, unplugt)
        s_percent = charge_data.iloc[k]['Starting SOC (%)']
        e_percent = charge_data.iloc[k]['Ending SOC (%)']
        #delta_time = e_dt-s_dt
        hrs_charging = mins_charging/60
        delta_perc = e_percent-s_percent
        if(hrs_charging >=0):
            if(hrs_charging <=10):
                if(delta_perc >0):
                    if(delta_perc >= 4.5*hrs_charging):
                        delta_charge_list.append(delta_perc)
                        delta_time_list.append(hrs_charging)
                        s_charge_list.append(s_percent)
                        e_charge_list.append(e_percent)
                        s_time_list.append(start_min)
                        ct_time_list.append(mins_charging)
        k=k-1
    lst = [delta_charge_list, delta_time_list]
    df = pd.DataFrame(columns=lst)
    df.to_excel('charge_vs_time.xlsx')
    #print(delta_time_list)
    #print(delta_charge_list)
    #fig, ax = plt.subplots()
    #ax.plot(delta_time_list, delta_charge_list, 'ro')
    #plt.title('charge time vs battery change')
    #plt.xlabel('change in time (hrs)')
    #plt.ylabel('change in charge')
    #plt.show()
    #return delta_time_list, 
    #chargevtime = sns.load_dataset()
    #sns.regplot(x=delta_time_list, y=delta_charge_list, data=df)
    return s_charge_list, e_charge_list, s_time_list, ct_time_list

charge_time()
