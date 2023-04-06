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
#m = Fitter(mile_list, distributions = get_common_distributions)
b = Fitter(mile_list, distributions =get_distributions())
#m.fit()
b.fit()
b.summary()
#print(b.summary())
print(b.get_best())
#m.summary()
#p is also weibull max, also 100% fit
#p=Fitter(kwh_list, distributions = get_distributions())
#b = Fitter(kwh_list, distributions= get_common_distributions())
#p.fit()
#b.fit()
# miles distribution has result: 
#{'laplace_asymmetric': {'kappa': 0.5656655470214752, 'loc': 49.999996346657085, 'scale': 17.774262322316076}}
#                    sumsquare_error          aic  ...  ks_statistic     ks_pvalue
#laplace_asymmetric         0.012449  1147.093302  ...      0.113783  5.951570e-16
#skewcauchy                 0.012786  1170.106471  ...      0.108861  1.233037e-14
#genhyperbolic              0.012995  1143.872285  ...      0.093344  7.192289e-11
#skewnorm                   0.013152  1143.084097  ...      0.093521  6.565197e-11
#norminvgauss               0.013155  1145.582101  ...      0.097566  7.760917e-12
#perc_used dist has this result:
#         sumsquare_error          aic           bic  kl_div  ks_statistic  ks_pvalue
#burr            0.005044  1007.320328 -17166.656251     inf      0.023443   0.430457
#burr12          0.005054  1006.171593 -17164.015539     inf      0.025368   0.333927
#mielke          0.005072  1006.768516 -17159.128846     inf      0.029277   0.185890
#maxwell         0.005103  1007.740968 -17165.179392     inf      0.035838   0.057228
#alpha           0.005113  1001.874430 -17155.364857     inf      0.029908   0.167711
#p prints best as dgamma w/ sumsquare error 1.49, 
#{'dgamma': {'a': 1.2217446905399747, 'loc': 1.8631753076526738, 'scale': 0.20790660522673732}}
#         sumsquare_error          aic          bic  kl_div  ks_statistic  ks_pvalue
#dgamma           1.493076  1224.668116 -9355.382704     inf      0.043843   0.009856
#dweibull         1.629590  1308.231042 -9235.171549     inf      0.044877   0.007652
#burr12           1.663234   912.843764 -9199.867763     inf      0.037152   0.043933
#fisk             1.665211   914.210653 -9205.461166     inf      0.037213   0.043381
#burr             1.665592   921.637504 -9197.921351     inf      0.036481   0.050346
#fig, ax = plt.subplots(1,1)
#x = kwh_list
#y= dgamma.pdf(kwh_list, 1.2217446905399747, 1.8631753076526738, 0.20790660522673732)
#ax.plot(x, y, "ro")
#n_bins = 100
#ax.hist(x, n_bins)
#plt.title('kwh histogram')
#plt.xlabel('List of kwh vals')
#plt.ylabel('# of appearances')
#print(p.summary())
#print(p.get_best())
#print(b.summary())
#print(b.get_best())
#plt.show()

#b prints lognorm w/ sumsquare of 1.92
#{'lognorm': {'s': 0.20515075436948102, 'loc': 0.28822691267682377, 'scale': 1.5888141586761089}}

#overall, best fit for kwh is a dgamma distribution!

