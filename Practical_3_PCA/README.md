# Practical 3: Principal Component Analysis (PCA)

## Objective
To reduce the dimensionality of the Breast Cancer dataset using PCA implemented from scratch with NumPy.

## Description
PCA is an unsupervised dimensionality reduction technique. It transforms correlated features into a smaller set of uncorrelated components (principal components) that capture the maximum variance in the data. Implemented manually without sklearn's PCA to understand the underlying math.

## Steps Performed
1. Load the Breast Cancer dataset (569 samples, 30 features)
2. Standardize features (zero mean, unit variance)
3. Compute the covariance matrix
4. Perform eigen decomposition (`np.linalg.eig`)
5. Sort eigenvectors by descending eigenvalues
6. Compute cumulative explained variance
7. Determine number of components for ≥50% variance
8. Plot the Scree Plot

## Libraries Used
- `numpy` — Eigen decomposition and linear algebra
- `pandas` — DataFrame handling
- `scikit-learn` — Breast Cancer dataset loader
- `matplotlib` / `seaborn` — Visualization

## How to Run
```bash
pip install numpy pandas scikit-learn matplotlib seaborn
python practical3.py
```

## Key Output
- Covariance matrix heatmap
- Eigenvalues and eigenvector shapes
- Number of components needed for ≥50% explained variance
- Scree plot of cumulative variance
