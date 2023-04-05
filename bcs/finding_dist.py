import pandas as pd
from fitter import Fitter, get_distributions, get_common_distributions
from scipy.stats import dgamma
import numpy as np
import matplotlib.pyplot as plt
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
#b = Fitter(kwh_list, distributions= get_common_distributions())
#p.fit()
#b.fit()
#p prints best as dgamma w/ sumsquare error 1.49, 
#{'dgamma': {'a': 1.2217446905399747, 'loc': 1.8631753076526738, 'scale': 0.20790660522673732}}
#         sumsquare_error          aic          bic  kl_div  ks_statistic  ks_pvalue
#dgamma           1.493076  1224.668116 -9355.382704     inf      0.043843   0.009856
#dweibull         1.629590  1308.231042 -9235.171549     inf      0.044877   0.007652
#burr12           1.663234   912.843764 -9199.867763     inf      0.037152   0.043933
#fisk             1.665211   914.210653 -9205.461166     inf      0.037213   0.043381
#burr             1.665592   921.637504 -9197.921351     inf      0.036481   0.050346
fig, ax = plt.subplots(1,1)
x = kwh_list
y= dgamma.pdf(kwh_list, 1.2217446905399747, 1.8631753076526738, 0.20790660522673732)
ax.plot(x, y, "ro")
ax.plot(x, x, "go")
#print(p.summary())
#print(p.get_best())
#print(b.summary())
#print(b.get_best())
plt.show()
#b prints lognorm w/ sumsquare of 1.92
#{'lognorm': {'s': 0.20515075436948102, 'loc': 0.28822691267682377, 'scale': 1.5888141586761089}}

#overall, best fit for kwh is a dgamma distribution!

