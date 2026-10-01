import pandas as pd

df = pd.read_csv("output/sales_data.csv")

print("Total Revenue:", round(df["Revenue"].sum(), 2))
print()
print("Revenue by Category:")
print(df.groupby("Category")["Revenue"].sum().round(2).sort_values(ascending=False))
print()
print("Revenue by Region:")
print(df.groupby("Region")["Revenue"].sum().round(2).sort_values(ascending=False))
print()
print("Top 5 Products by Revenue:")
print(df.groupby("Product")["Revenue"].sum().round(2).sort_values(ascending=False).head(5))
print()
print("Orders by Payment Mode:")
print(df["PaymentMode"].value_counts())