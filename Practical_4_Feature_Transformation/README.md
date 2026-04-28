# Practical 4: Feature Transformation

## Objective
To apply various mathematical feature transformation techniques on a numeric dataset and observe their effects.

## Description
Feature transformation converts raw feature values into new representations better suited for machine learning models. It helps handle skewed distributions, compress large value ranges, and expose hidden patterns in data.

## Transformations Covered
| Transformation | Formula | Use Case |
|---|---|---|
| Logarithmic | `log(1 + x)` | Reduce right-skewed distributions |
| Square | `x²` | Amplify differences between large values |
| Reciprocal | `1/x` | Compress large values, invert relationships |
| Sine | `sin(x)` | Model cyclic/periodic patterns |
| Cosine | `cos(x)` | Model cyclic/periodic patterns |
| Tangent | `tan(x)` | Angular data transformations |
| Square Root | `√x` | Moderate right-skew correction |

## Libraries Used
- `numpy` — Mathematical transformation operations
- `pandas` — Result display as DataFrame
- `scikit-learn` — `FunctionTransformer` wrapper

## How to Run
```bash
pip install numpy pandas scikit-learn
python practical4.py
```

## Sample Output
A comparison table showing values [1, 2, 3, 4, 5, 6] after each transformation side by side.
