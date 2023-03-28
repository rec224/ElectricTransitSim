import pandas as pd
from fitter import Fitter, get_distributions, get_common_distributions
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
print(dataframe1)
# here we are getting the miles traveled and the percentage battery used from the actual vta data
i=0
mile_list = []
perc_used_list =[]
kwh_list=[]
while(i<1374):
     cell1 = dataframe1.iloc[i]['miles_travelled']
     mile_list.append(cell1)
     cell2 = dataframe1.iloc[i]['percent_used']
     perc_used_list.append(cell2)
     cell3 = dataframe1.iloc[i]['kwh']
     kwh_list.append(cell3)
     i= i+1
#print(mile_list)
#print(perc_used_list)
#m is weibell max distribution, 100% fit 
#m = Fitter(mile_list)
#m.fit()
#m.summary()
#p is also weibull max, also 100% fit
#p=Fitter(kwh_list, distributions = get_distributions())
b = Fitter(kwh_list, distributions= get_common_distributions())
#p.fit()
b.fit()
#p prints best as dgamma w/ sumsquare error 1.49, 
#{'dgamma': {'a': 1.2217446905399747, 'loc': 1.8631753076526738, 'scale': 0.20790660522673732}}
#print(p.summary())
#print(p.get_best())
print(b.summary())
print(b.get_best())
#b prints lognorm w/ sumsquare of 1.92
#{'lognorm': {'s': 0.20515075436948102, 'loc': 0.28822691267682377, 'scale': 1.5888141586761089}}

#overall, best fit for kwh is a dgamma distribution!

