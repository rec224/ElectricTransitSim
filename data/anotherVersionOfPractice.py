# import csv

# # with open('Reports.csv', newline='') as csvfile:
# #     data = list(csv.reader(csvfile))


# import pandas as pd
# import matplotlib.pyplot as plt


# data = pd.read_csv("Reports.csv")

# #data.plot(x = "DateTime", y = ['2600 - Energy used','2601 - Energy used','2602 - Energy used','2603 - Energy used','2604 - Energy used','2605 - Energy used','2606 - Energy used','2607 - Energy used','2608 - Energy used','2609 - Energy used','2610 - Energy used','2611 - Energy used','2612 - Energy used','2613 - Energy used'])
# plt.show()
# # kwc = data['DateTime'].tolist()
# # miles_travelled = data['2600 - Average speed'].tolist()
# # plt.plot(kwc, miles_travelled)
# # plt.show()

# # import numpy as np
# # import matplotlib.pyplot as plt
# # fig, ax = plt.subplots()
# # plt.title("Random")
# # plt.plot(xpoints, ypoints)
# # plt.show()
# import pandas as pd
# df = pd.read_csv('Reports1.csv')
# import csv
# import matplotlib.pyplot as plt
# arr = df.to_numpy()
# with open('Reports1.csv') as csv_file:
 
#     # creating an object of csv reader
#     # with the delimiter as ,
#     csv_reader = csv.reader(csv_file, delimiter = ',')
 
#     # list to store the names of columns
#     list_of_column_names = []
 
#     # loop to iterate through the rows of csv
#     for row in csv_reader:
 
#         # adding the first row
#         list_of_column_names.append(row)
 
#         # breaking the loop after the
#         # first iteration itself
#         break
# color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
# counter = 0
# for i in range(0,70,5):
#     x = arr[:,i+1]
#     y = arr[:,i+2]
#     plt.scatter(x,y, 3, color[counter])
    
#     counter = counter +1
# plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
    
# plt.xlabel("Number of charging sessions")
# plt.ylabel("Distance Driven")
# plt.xlim(0,60)
# plt.ylim(0,20)
# plt.show()
# import pandas as pd
# df = pd.read_csv('bigCSV.csv')
# import csv
# import matplotlib.pyplot as plt
# arr = df.to_numpy()
# with open('bigCSV.csv') as csv_file:
 
#     # creating an object of csv reader
#     # with the delimiter as ,
#     csv_reader = csv.reader(csv_file, delimiter = ',')
 
#     # list to store the names of columns
#     list_of_column_names = []
 
#     # loop to iterate through the rows of csv
#     for row in csv_reader:
 
#         # adding the first row
#         list_of_column_names.append(row)
 
#         # breaking the loop after the
#         # first iteration itself
#         break
# color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
# counter = 0
# for i in range(0,168,12):
#     x = arr[:,i+6]
#     y = arr[:,i+10]
#     plt.scatter(x,y, 3, color[counter])
#     counter = counter +1
# plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
# plt.xlabel("Energy Used")
# plt.ylabel("Distance Driven")
# plt.show()
# import seaborn
# import pandas as pd
# df = pd.read_csv('bigCSV.csv')
# import csv
# import matplotlib.pyplot as plt
# arr = df.to_numpy()
# color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
# counter = 0
# labels = ["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"]


# for i in range(0,168,12):
#     x = arr[:,i+9]
#     y = arr[:,i+10]
#     csv = pd.read_csv(r'bigCSV.csv')
#     res = seaborn.scatterplot(x=x, y=y, data=csv, label = labels[counter] ,color = color[counter])
#     counter = counter +1
# res.set_title("Seaborn example")
# res.set_xlabel("Energy Used")
# res.set_ylabel("Distance Driven")
# #res.legend(labels = ["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
# plt.show()

# import pandas as pd
# df = pd.read_csv('Reports.csv')
# import csv
# import matplotlib.pyplot as plt
# arr = df.to_numpy()
# with open('Reports.csv') as csv_file:
 
#     # creating an object of csv reader
#     # with the delimiter as ,
#     csv_reader = csv.reader(csv_file, delimiter = ',')
 
#     # list to store the names of columns
#     list_of_column_names = []
 
#     # loop to iterate through the rows of csv
#     for row in csv_reader:
 
#         # adding the first row
#         list_of_column_names.append(row)
 
#         # breaking the loop after the
#         # first iteration itself
#         break
# color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
# counter = 0
# for i in range(0,126,9):
#     x = arr[:,i+8]
#     y = arr[:,i+7]

#     plt.scatter(x,y, 3, color[counter])
    
#     counter = counter +1
# plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
    
# plt.xlabel("Distance driven(miles)")
# plt.ylabel("HVAC Inverter DCP Energy used")

# plt.show()
import pandas as pd
df = pd.read_csv('ReportsAir.csv')
import csv
import matplotlib.pyplot as plt
arr = df.to_numpy()
with open('ReportsAir.csv') as csv_file:
 
    # creating an object of csv reader
    # with the delimiter as ,
    csv_reader = csv.reader(csv_file, delimiter = ',')
 
    # list to store the names of columns
    list_of_column_names = []
 
    # loop to iterate through the rows of csv
    for row in csv_reader:
 
        # adding the first row
        list_of_column_names.append(row)
 
        # breaking the loop after the
        # first iteration itself
        break
color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
counter = 0
for i in range(0,126,9):
    x = arr[:,i+9]
    y = arr[:,i+1]
    plt.scatter(x,y, 3, color[counter])
    
    counter = counter +1
plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
    
plt.xlabel("Time Driving(hours)")
plt.ylabel("Air Compressor Energy used(kWh)")
plt.show()

# import pandas as pd
# df = pd.read_csv('vta energy consumption data.csv')
# import csv
# import matplotlib.pyplot as plt
# arr = df.to_numpy()
# with open('Reports.csv') as csv_file:
 
#     # creating an object of csv reader
#     # with the delimiter as ,
#     csv_reader = csv.reader(csv_file, delimiter = ',')
 
#     # list to store the names of columns
#     list_of_column_names = []
 
#     # loop to iterate through the rows of csv
#     for row in csv_reader:
 
#         # adding the first row
#         list_of_column_names.append(row)
 
#         # breaking the loop after the
#         # first iteration itself
#         break
# color = ["b","b","b","b","b","b","b","b","b","b","b", "b", "b", "b"]
# counter = 0
# x = arr[:,5]
# y = arr[:,7]
# plt.scatter(x,y, 3)
  
# plt.xlabel("Energy Used")
# plt.ylabel("Distance")
# plt.show()
