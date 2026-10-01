import os
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/sales_data.csv")
os.makedirs("output/charts", exist_ok=True)

# Chart 1: Revenue by Category
cat = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
cat.plot(kind="bar", color="steelblue")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/charts/revenue_by_category.png")
plt.close()

# Chart 2: Revenue by Region
reg = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
reg.plot(kind="bar", color="seagreen")
plt.title("Revenue by Region")
plt.ylabel("Revenue")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/charts/revenue_by_region.png")
plt.close()

# Chart 3: Monthly Revenue Trend
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
monthly = df.groupby(df["OrderDate"].dt.month)["Revenue"].sum()
plt.figure(figsize=(8, 5))
monthly.plot(kind="line", marker="o", color="darkorange")
plt.title("Monthly Revenue Trend (2025)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.savefig("output/charts/monthly_revenue.png")
plt.close()

print("Charts saved in output/charts/")