# Practical 5: Feature Selection

## Objective
To select the most relevant features from the Wine dataset using three categories of feature selection methods: Filter, Wrapper, and Embedded.

## Description
Feature selection reduces dimensionality by removing irrelevant or redundant features. This improves model accuracy, reduces overfitting, speeds up training, and makes models more interpretable.

## Methods Covered

### 1. Filter Methods (score-based, model-independent)
| Method | Technique | Function |
|---|---|---|
| Information Gain | ANOVA F-value | `f_classif` |
| Chi-square Test | Statistical test | `chi2` |
| Correlation Coefficient | Pearson correlation | `corrwith` |
| Variance Threshold | Remove low-variance features | `VarianceThreshold` |
| Mean Absolute Difference | Spread-based scoring | Custom lambda |

### 2. Wrapper Methods (model-based search)
| Method | Direction | Function |
|---|---|---|
| Forward Selection | Starts empty, adds features | `SequentialFeatureSelector(forward=True)` |
| Backward Elimination | Starts full, removes features | `SequentialFeatureSelector(forward=False)` |
| RFE | Recursive pruning | `RFE` with Logistic Regression |

### 3. Embedded Methods (learn importance during training)
| Method | Algorithm | Function |
|---|---|---|
| Lasso Regularization | L1 penalty | `LassoCV` |
| Tree-based Importance | Feature importance scores | `RandomForestClassifier` |

## Libraries Used
- `scikit-learn` — Models, feature selectors, dataset
- `mlxtend` — Sequential Feature Selector
- `pandas`, `numpy` — Data handling

## How to Run
```bash
pip install scikit-learn mlxtend pandas numpy
python practical5.py
```
