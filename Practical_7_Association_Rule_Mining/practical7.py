# PRACTICAL 7: Association Rule Mining

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Transaction dataset
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread', 'butter', 'jam'],
    ['butter', 'jam']
]

print("Transactions:")
for i, t in enumerate(dataset):
    print(f"  T{i+1}: {t}")

# Step 1: Encode transactions into one-hot format
te = TransactionEncoder()
te_array = te.fit_transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)
print("\nEncoded DataFrame:")
print(df)

# Step 2: Apriori — find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print("\nFrequent Itemsets (min_support=0.6):")
print(frequent_itemsets)

# Step 3: Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
print("\nAssociation Rules (min_confidence=0.7):")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
