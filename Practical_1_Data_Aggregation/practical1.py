# PRACTICAL 1: Data Aggregation and Its Types

import pandas as pd

# Step 1: Create Sample Dataset
datasak = {
   'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
   'Product': ['A', 'B', 'A', 'B', 'C', 'C', 'B', 'A'],
   'Sales': [150, 200, 300, 400, 250, 180, 220, 310],
   'Quantity': [10, 15, 20, 25, 12, 14, 16, 18]
}

df = pd.DataFrame(datasak)
print("Sample Dataset:\n", df)

# Sum aggregation
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", sales_by_region)

# Mean aggregation
mean_by_product = df.groupby('Product')[['Sales', 'Quantity']].mean()
print("\nMean Sales and Quantity by Product:\n", mean_by_product)

# Count aggregation
count_by_region = df.groupby('Region')['Sales'].count()
print("\nCount of Sales Records by Region:\n", count_by_region)

# Custom aggregation (min, max)
custom_aggregation = df.groupby('Region')['Sales'].agg(['min', 'max'])
print("\nCustom Aggregation (Min/Max Sales by Region):\n", custom_aggregation)

# Multi-level aggregation
multi_level_agg = df.groupby(['Region', 'Product'])['Sales'].sum()
print("\nSales by Region and Product:\n", multi_level_agg)

# Reset index
multi_level_agg_reset = multi_level_agg.reset_index()
print("\nAfter Reset Index:\n", multi_level_agg_reset)
