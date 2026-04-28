# Practical 7: Association Rule Mining

## Objective
To discover frequent itemsets and generate association rules from a market basket dataset using the Apriori algorithm.

## Description
Association rule mining finds interesting relationships between variables in large databases. It is widely used in market basket analysis to determine which products are frequently bought together, enabling recommendations and store layout decisions.

## Key Concepts
| Term | Definition | Formula |
|---|---|---|
| Support | Frequency of an itemset in all transactions | `count(A) / total transactions` |
| Confidence | How often the rule holds true | `support(A∪B) / support(A)` |
| Lift | Strength of rule over random chance | `confidence(A→B) / support(B)` |

## Algorithm
- **Apriori** — Generates frequent itemsets using the anti-monotone property: if an itemset is infrequent, all its supersets are also infrequent (pruning).

## Parameters Used
| Parameter | Value | Meaning |
|---|---|---|
| `min_support` | 0.6 | Item must appear in ≥60% of transactions |
| `min_confidence` | 0.7 | Rule must be correct ≥70% of the time |

## Libraries Used
- `mlxtend` — `apriori`, `association_rules`, `TransactionEncoder`
- `pandas` — DataFrame handling

## How to Run
```bash
pip install mlxtend pandas
python practical7.py
```

## Sample Output
- Frequent itemsets: `{bread}`, `{butter}`, `{bread, butter}`, etc.
- Rules example: `{bread} → {butter}` with support=0.75, confidence=1.0, lift=1.33
