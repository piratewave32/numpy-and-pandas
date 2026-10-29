import pandas as pd
import numpy as np


df = pd.read_csv("expense.csv")

df["Total"] = df(["Amount"], errors = "coerce").cumsum()
df["Average"] = df["Amount"].mean()
df["Maximum Spend in month"] = df["Amount"].max()
df["level"] = np.where(df["Amount"]>df["Average"],"High","Low")
df.to_csv("expense.csv",index = False)
