import pandas as pd

# Load all CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine all data
df = pd.concat([df1, df2, df3])

# Filter only Pink Morsel
df = df[df["product"] == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep required columns
df = df[["sales", "date", "region"]]

# Save output
df.to_csv("processed_data.csv", index=False)

print("Data processing completed!")