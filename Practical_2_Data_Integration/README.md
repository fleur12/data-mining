# Practical 2: Data Integration and Data Transformation for Data Mining

## Objective
To perform data integration by merging multiple datasets and apply various data transformation techniques.

## Description
Data integration combines data from different sources into a unified view. Data transformation converts raw data into a format suitable for mining. Both are critical preprocessing steps in any data mining pipeline.

## Techniques Covered
| Technique | Description |
|---|---|
| Tight Coupling | Inner join — only matching records from both datasets |
| Loose Coupling | Outer join — all records, NaN for missing values |
| Smoothing | Rolling/moving average to reduce noise in Age |
| Aggregation | Summarizing Salary by Gender |
| Discretization | Binning continuous Age into categorical groups |
| Attribute Construction | Creating a new Age-to-Salary Ratio feature |

## Libraries Used
- `pandas` — Data manipulation and merging
- `numpy` — Numerical operations

## How to Run
```bash
pip install pandas numpy
python practical2.py
```

## Sample Output
- Inner and outer merged datasets
- Smoothed age using rolling window of 2
- Age grouped into: Teen / Young Adult / Adult / Senior
- New derived feature: Age_Salary_Ratio
