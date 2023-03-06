import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dfm = pd.read_csv("../ReportsTimDis.csv")
vir_arr = dfm.to_numpy() 

datafm = pd.read_csv("../vta energy consumption data.csv")
vta_arr = datafm.to_numpy() 

vir_en = np.array([])
vir_dt = np.array([])
for i in range(0, 28,2):
    vir_en = np.concatenate((vir_en, vir_arr[:, i+1]));
    vir_dt = np.concatenate((vir_dt, vir_arr[:, i+2]));

vir_ef = vir_en/vir_dt;
filterArr = []
for val in vir_en:
    if(val < 1000):
        filterArr.append(True)
    else:
        filterArr.append(False)
plt.hist(vir_en[filterArr])
plt.xlabel("Energy used per day (kWh)")
plt.title("Viriciti data: energy used per day (kWh)")
mean = round(vir_en[filterArr].mean(),2)
plt.text(mean,1500, "| Mean: " + str(mean))
plt.text(mean, 1450, "| ")
plt.text(mean, 1400, "| ")
plt.savefig("data/charts/Vir_en")
plt.show()

filterArr = []
for val in vir_ef:
    if(val < 10):
        filterArr.append(True)
    else:
        filterArr.append(False)
        
plt.hist(vir_ef[filterArr])
plt.xlabel("Energy/distance per day (kWh per mile)")
plt.title("Viriciti data: daily efficency (kWh/mile)")
mean = round(vir_ef[filterArr].mean(),2)
plt.text(mean,1500, "| Mean: " + str(mean))
plt.text(mean, 1400, "| ")
plt.text(mean, 1300, "| ")
plt.savefig("data/charts/Vir_ef")
plt.show()

vta_energy = vta_arr[:,5]*vta_arr[:,7]
filterArr = []
for val in vta_energy:
    if(val < 5000):
        filterArr.append(True)
    else:
        filterArr.append(False)
plt.hist(vta_energy[filterArr])
plt.xlabel("Energy used per day (kWh)")
plt.title("VTA data: energy used per day (kWh)")
mean = round(vta_energy[filterArr].mean(),2)
plt.text(mean,300, "| Mean: " + str(mean))
plt.text(mean, 290, "| ")
plt.text(mean, 280, "| ")
plt.savefig("data/charts/VTA_en")
plt.show()

plt.hist(vta_arr[:, 5])
plt.xlabel("Energy/distance per day (kWh per mile)")
plt.title("VTA data: daily efficency (kWh/mile)")
mean = round(vta_arr[:, 5].mean(),2)
plt.text(mean-0.25,420, "Mean: " + str(mean))
plt.text(mean,400, "| ")
plt.text(mean, 380, "| ")
plt.text(mean, 360, "| ")
plt.savefig("data/charts/VTA_ef")
plt.show()

vta_energy = np.array(datafm["kwh"])*np.array(datafm["miles_travelled"])

vir_en = np.array([])
for i in range(0, 14):
    pad = "0"
    if(i>9):
        pad = ""
    string = "26" + pad + str(i) + " - Energy used"
#     print(np.array(dfm[string]))
    vir_en = np.concatenate((vir_en, np.array(dfm[string])))

    
sns.kdeplot(vir_en, label = "Viricity", fill = True, color = 'r')
sns.kdeplot(vta_energy, label = "VTA", fill = True, color = 'b')
plt.legend()
plt.title("Comparison of energy consumption")
plt.xlabel("kWh")
plt.show()

vta_ef = np.array(datafm["kwh"])

vir_en = np.array([])
vir_dt = np.array([])
for i in range(0, 14):
    pad = "0"
    if(i>9):
        pad = ""
    e_string = "26" + pad + str(i) + " - Energy used"
    d_string = "26" + pad + str(i) + " - Distance driven"
    vir_en = np.concatenate((vir_en, np.array(dfm[e_string])))
    vir_dt = np.concatenate((vir_dt, np.array(dfm[d_string])))
vir_ef = vir_en/vir_dt
filterArr = []
for val in vir_ef:
    if(val < 6):
        filterArr.append(True)
    else:
        filterArr.append(False)
vir_ef = vir_ef[filterArr]
    
sns.kdeplot(vir_ef, label = "Viricity", fill = True, color = 'r')
sns.kdeplot(vta_ef, label = "VTA", fill = True, color = 'b')
plt.legend()
plt.title("Comparison of efficency")
plt.xlabel("kWh/mile")
plt.show()