import pandas as pd
from fitter import Fitter
dataframe1 = pd.read_excel('clean_drive_data.xlsx')
print(dataframe1)
# here we are getting the miles traveled and the percentage battery used from the actual vta data
i=0
mile_list = []
perc_used_list =[]
while(i<1374):
     cell1 = dataframe1.iloc[i]['miles_travelled']
     mile_list.append(cell1)
     cell2 = dataframe1.iloc[i]['percent_used']
     perc_used_list.append(cell2)
     i= i+1
print(mile_list)
print(perc_used_list)
#m is weibell max distribution, 100% fit 
#m = Fitter(mile_list)
#m.fit()
#m.summary()
#p is also weibull max, also 100% fit
p=Fitter(perc_used_list)
p.fit()
p.summary()
