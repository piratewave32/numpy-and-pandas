import numpy as np 
import pandas as pd 

steps = np.random.randint(3000,12000,35)
week = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
days = (week*5)[:35]
goal = np.random.randint(3000,12000,35)

df = pd.DataFrame({"Steps":steps,"Days":days,"Goals":goal})

#Numpy round off calculation

df["KM"] = np.round(df["Steps"]*0.0008,2)
df["Calorie"] = (df["Steps"]*0.04)
df["Status"] = np.where(df["Steps"]>df["Goals"],"Completed","Failed")

print(df)
print("\nTotal steps\n",steps.sum())
print("\nAverage is\n",steps.mean())
print(df["Steps"].describe())
