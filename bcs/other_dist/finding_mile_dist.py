import pandas as pd
from fitter import Fitter, get_distributions
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
print(dataframe1)
# here we are getting the miles traveled and the percentage battery used from the actual vta data
i=0
mile_list = []
while(i<1374):
     cell1 = dataframe1.iloc[i]['miles_travelled']
     mile_list.append(cell1)
     i= i+1
print(mile_list)
b = Fitter(mile_list, distributions =get_distributions())
b.fit()
print(b.summary())
print(b.get_best())
# miles distribution has result: 
#{'laplace_asymmetric': {'kappa': 0.5656655470214752, 'loc': 49.999996346657085, 'scale': 17.774262322316076}}
#                    sumsquare_error          aic  ...  ks_statistic     ks_pvalue
#laplace_asymmetric         0.012449  1147.093302  ...      0.113783  5.951570e-16
#skewcauchy                 0.012786  1170.106471  ...      0.108861  1.233037e-14
#genhyperbolic              0.012995  1143.872285  ...      0.093344  7.192289e-11
#skewnorm                   0.013152  1143.084097  ...      0.093521  6.565197e-11
#norminvgauss               0.013155  1145.582101  ...      0.097566  7.760917e-12

