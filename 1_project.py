import pandas as pd
import numpy as np


data = {"Name":["Ram","Hari","Shyam","Sita","Pikachu"],
         "Roll_no":[1,2,3,4,5],
         "Math":[40,10,90,20,99],
         "Science":[80,80,90,56,65],
         "English":[60,70,80,60,60],
         "Nepali":[50,40,60,80,90]
         
    }

df = pd.DataFrame(data)
scores = df[["Math","Science","English","Nepali"]].to_numpy()
df["Total"] = np.sum(scores,axis = 1)
df["Average"] = np.round(np.mean(scores,axis =1),2)


#for pass or fail
df["Result"] = np.where(df["Average"]>40,"Pass","Fail")
df["Rank"] = df["Total"].rank(ascending=False).astype(int)
df = df.sort_values("Rank")

with pd.ExcelWriter("grade.xlsx") as writer:
    df.to_excel(writer,sheet_name="student",index=False)

print("data saved")
    