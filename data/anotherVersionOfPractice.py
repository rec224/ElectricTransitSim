import pandas as pd
df = pd.read_csv('bigCSV.csv')
arr = df.to_numpy()
new = pd.DataFrame(arr)
print(new)

with open('bigCSV.csv') as csv_file:
 
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
list_of_column_names[0][9]

#Version 1
color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
counter = 0
for i in range(0,168,12):
    x = arr[:,i+6]
    y = arr[:,i+10]
    plt.scatter(x,y, 3, color[counter])
    counter = counter +1
plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
    
plt.xlabel("Energy Used")
plt.ylabel("Distance Driven")

#Version 2
for i in range(0,84,6):
    x = arr[:,i+1]
    y = arr[:,i+6]
    plt.scatter(x,y, 3, color[counter])
    
    counter = counter +1
plt.legend(["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
    
plt.xlabel("Number of charging sessions")
plt.ylabel("Distance Driven")
plt.xlim(0,1.1)
plt.show()

# this is with seaborn
import seaborn
import pandas as pd
df = pd.read_csv('bigCSV.csv')
import csv
import matplotlib.pyplot as plt
arr = df.to_numpy()
color = ["b","r","g","c","m","y","k","fuchsia","lightgreen","darkgoldenrod","lightsteelblue", "blueviolet", "darkorange", "bisque"]
counter = 0
labels = ["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"]


for i in range(0,168,12):
    x = arr[:,i+9]
    y = arr[:,i+10]
    csv = pd.read_csv(r'bigCSV.csv')
    res = seaborn.scatterplot(x=x, y=y, data=csv, label = labels[counter] ,color = color[counter])
    counter = counter +1
res.set_title("Seaborn example")
res.set_xlabel("Energy Used")
res.set_ylabel("Distance Driven")
#res.legend(labels = ["2600", "2601", "2602", "2603", "2604", "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613"])
plt.show()

