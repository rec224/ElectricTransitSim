import pandas as pd
from fitter import Fitter, get_distributions
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
print(dataframe1)
# here we are getting the percentage battery used from the actual vta data
i=0
perc_used_list =[]
while(i<1374):
     cell2 = dataframe1.iloc[i]['percent_used']
     perc_used_list.append(cell2)
     i= i+1
print(perc_used_list)
p = Fitter(perc_used_list, distributions =get_distributions())
p.fit()
print(p.summary())
print(p.get_best())
#perc_used dist has this result:
#         sumsquare_error          aic           bic  kl_div  ks_statistic  ks_pvalue
#burr            0.005044  1007.320328 -17166.656251     inf      0.023443   0.430457
#burr12          0.005054  1006.171593 -17164.015539     inf      0.025368   0.333927
#mielke          0.005072  1006.768516 -17159.128846     inf      0.029277   0.185890
#maxwell         0.005103  1007.740968 -17165.179392     inf      0.035838   0.057228
#alpha           0.005113  1001.874430 -17155.364857     inf      0.029908   0.167711