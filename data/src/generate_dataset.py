import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

NUM_RECORDS = 2000

products = {
    "Laptop": "Electronics", "Smartphone": "Electronics", "Headphone": "Electronics",
    "Office Chair": "Furniture", "Desk": "Furniture", "Bookshelf": "Furniture",
    "T-Shirt": "Apparel", "Jeans": "Apparel", "Jacket": "Apparel",
    "Notebook": "Stationery", "Pen Set": "Stationery"
}

price_range = {
    "Laptop": (30000, 80000), "Smartphone": (10000, 60000), "Headphone": (500, 5000),
    "Office Chair": (2000, 12000), "Desk": (3000, 15000), "Bookshelf": (1500, 8000),
    "T-Shirt": (300, 1500), "Jeans": (800, 3000), "Jacket": (1500, 6000),
    "Notebook": (50, 300), "Pen Set": (50, 500)
}

regions = ["North", "South", "East", "West"]
payment_modes = ["Credit Card", "UPI", "Cash", "Net Banking"]

start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 12, 31)
date_range_days = (end_date - start_date).days

rows = []

for i in range(NUM_RECORDS):
    product = random.choice(list(products.keys()))
    category = products[product]
    random_days = random.randint(0, date_range_days)
    order_date = start_date + timedelta(days=random_days)
    quantity = random.randint(1, 10)
    low, high = price_range[product]
    unit_price = round(random.uniform(low, high), 2)
    revenue = round(unit_price * quantity, 2)
    rows.append({
        "OrderID": f"ORD{1000+i}",
        "OrderDate": order_date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Region": random.choice(regions),
        "PaymentMode": random.choice(payment_modes),
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "Revenue": revenue
    })

df = pd.DataFrame(rows)
os.makedirs("output", exist_ok=True)
df.to_csv("output/sales_data.csv", index=False)

print("Dataset generated successfully!")
print(df.shape)
print(df.head())