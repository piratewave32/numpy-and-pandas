import pandas as pd
import numpy as np

rng = np.random.default_rng(1)
veg =  ["Tomato", "Potato", "Onion", "Cauli", "Spinach"]
weeks =[f"Week {i}" for i in range(1,11)]

#base price of vegetables
base_price = [20,30,35,25,30]
change = rng.integers(50, 100, size=(10,5))
prices = change.cumsum(axis=0) + base_price

df = pd.DataFrame(prices, index=weeks, columns=veg)

summary = pd.DataFrame({
    "Mean Price": df.mean(),    
    "Max Price": df.max(),
    "Min Price": df.min(),
    "Price Range": df.max() - df.min(),
    "Cheapest Week": df.idxmin(),
    "Most Expensive Week": df.idxmax()
})
summary.to_csv("vegetable_summary.csv")
summary["Change%"] = ((summary["Max Price"] - summary["Min Price"]) / summary["Mean Price"]* 100).round(1)

print("Vegetable Price Summary")
print(summary)
print("Most Expensive Vegetable:",df.std().idxmax())
print("Cost of Each week ",df.sum(axis=1).to_string())

