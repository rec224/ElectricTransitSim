import pandas as pd
from fitter import Fitter, get_distributions
from scipy.stats import dgamma
import matplotlib.pyplot as plt
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
#print(dataframe1)
# here we are getting the kwh used from the actual vta data
i=0
kwh_list=[]
while(i<1374):
     cell3 = dataframe1.iloc[i]['kwh']
     kwh_list.append(cell3)
     i= i+1
k = Fitter(kwh_list, distributions =get_distributions())
k.fit()
print(k.summary())
print(k.get_best())

#k prints best as dgamma w/ sumsquare error 1.49, 
#{'dgamma': {'a': 1.2217446905399747, 'loc': 1.8631753076526738, 'scale': 0.20790660522673732}}
#         sumsquare_error          aic          bic  kl_div  ks_statistic  ks_pvalue
#dgamma           1.493076  1224.668116 -9355.382704     inf      0.043843   0.009856
#dweibull         1.629590  1308.231042 -9235.171549     inf      0.044877   0.007652
#burr12           1.663234   912.843764 -9199.867763     inf      0.037152   0.043933
#fisk             1.665211   914.210653 -9205.461166     inf      0.037213   0.043381
#burr             1.665592   921.637504 -9197.921351     inf      0.036481   0.050346

