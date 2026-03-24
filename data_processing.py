import pandas as pd

# List of files
files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

# Load and combine all files
df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

# Filter only Pink Morsel (case insensitive)
df = df[df["product"].str.lower() == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Select required columns
df = df[["sales", "date", "region"]]

# Optional: Rename columns (professional touch)
df.rename(columns={
    "sales": "Sales",
    "date": "Date",
    "region": "Region"
}, inplace=True)

# Save processed data
df.to_csv("processed_data.csv", index=False)

print("Data processing completed successfully!")