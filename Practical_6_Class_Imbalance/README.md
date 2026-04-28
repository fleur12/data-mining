# Practical 6: Class Imbalance Handling

## Objective
To handle class imbalance in a binary classification dataset using manual upsampling and `imblearn`'s `RandomOverSampler`.

## Description
Class imbalance occurs when one class significantly outnumbers another (e.g., 80% vs 20%). This causes models to be biased toward the majority class, ignoring the minority class. Oversampling techniques help balance the distribution before training.

## Techniques Covered
| Technique | Method | Description |
|---|---|---|
| Manual Upsampling | `sklearn.utils.resample` | Randomly duplicate minority class samples with replacement |
| RandomOverSampler | `imblearn` | Automated random oversampling to balance classes |

## Dataset
- Synthetically generated using `make_classification`
- 100 samples, 4 features, 2 classes
- Class 0: ~80 samples (majority), Class 1: ~20 samples (minority)

## Libraries Used
- `scikit-learn` — `make_classification`, `resample`
- `imbalanced-learn` — `RandomOverSampler`
- `pandas` — Data handling

## How to Run
```bash
pip install scikit-learn imbalanced-learn pandas
python practical6.py
```

## Sample Output
```
Original:         Class 0 = 80, Class 1 = 20
After resample:   Class 0 = 80, Class 1 = 80
After imblearn:   Class 0 = 80, Class 1 = 80
```
