import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

home = ["H106","H109","H208","H209","H309"]
previous_month = np.array([150,250,400,80,90])
current_month = np.array([300,450,600,285,250])

rate = 25
unit =current_month-previous_month
services = 100
bill = pd.DataFrame({"Home":home,"Units":unit})
bill["Energy"] = unit*rate
bill["After the service"] = bill["Energy"]+services
bill["After the service&tax"] = (bill["After the service"]*1.13).round(2)
bill["Charge for coustomer above 200 unit "] = np.where(unit>200,bill["After the service&tax"]+50,bill["After the service&tax"])
bill["Total Amount"] = bill["Charge for coustomer above 200 unit "]
bill = bill.sort_values("Total Amount",ascending=False)
bill["Average Spending "] = bill["Total Amount"].mean()


order =np.argsort(previous_month)
x_axis = previous_month[order]
y_axis = current_month[order]

plt.subplot(1,2,1)
plt.xlabel("Previous Month")
plt.ylabel("Current Month")
plt.title("Unit Consumption")
plt.plot(x_axis,y_axis,'o:r',markersize =10,mec="r",mfc="g")


l_axis = bill["Energy"]
z_axis =bill["Total Amount"]

plt.grid(color="b",linestyle="--",linewidth=0.5)
plt.subplot(1,2,2)
plt.title("Spending Amount")
plt.xlabel("Energy Consumed")
plt.ylabel("Total Amount")

plt.plot(l_axis,z_axis,'o:r',markersize =10,mec="r",mfc="g")



plt.suptitle("Electricity Bill Record",fontsize=20)
plt.grid(color="b",linestyle="--",linewidth=0.5)

print("Houses above 200 units:", (bill["Units"] > 200).sum())
print("Total collected: Rs", bill["Total Amount"].sum())

bill.to_csv("Electric Bill Record.csv",index=False)
print("The data has been saved")
plt.show()