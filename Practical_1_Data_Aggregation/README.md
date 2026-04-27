# Practical 1: Data Aggregation and Its Types

## Objective
To understand and implement various types of data aggregation techniques using Python and Pandas.

## Description
Data aggregation is the process of compiling and summarizing data from multiple sources or records into a single, more meaningful dataset. It is a fundamental step in data mining and analytics, enabling pattern discovery and high-level insights from raw data.

## Techniques Covered
| Technique | Function Used | Purpose |
|---|---|---|
| Sum Aggregation | `groupby().sum()` | Total sales per region |
| Mean Aggregation | `groupby().mean()` | Average sales/quantity per product |
| Count Aggregation | `groupby().count()` | Number of records per region |
| Custom Aggregation | `groupby().agg(['min', 'max'])` | Min/max sales per region |
| Multi-level Aggregation | `groupby([col1, col2])` | Sales by region AND product |

## Libraries Used
- `pandas` — Data manipulation and groupby operations

## How to Run
```bash
pip install pandas
python practical1.py
```

## Sample Output
- Total sales grouped by region
- Mean sales and quantity grouped by product
- Custom min/max aggregation per region
- Multi-level groupby results with reset index
