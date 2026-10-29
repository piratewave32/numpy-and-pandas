import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Date": ["2026-10-01", "2026-10-01", "2026-10-02", "2026-10-03",
             "2026-10-03", "2026-10-04", "2026-10-05", "2026-10-05"],
    "Category": ["food", "bus", "food", "books", "food", "bus", "food", "books"],
    "Amount": [150, 40, 200, 500, 120, 60, 180, 250],
})

print(df.shape)
print(df[df["Amount"]>100])
print(df.sort_values("Amount"))