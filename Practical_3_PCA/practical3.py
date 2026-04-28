# PRACTICAL 3: PCA (Principal Component Analysis)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

# Load dataset
cancer = load_breast_cancer(as_frame=True)
df = cancer.frame

print('Original DataFrame shape:', df.shape)

X = df[cancer['feature_names']]
print('Inputs dataframe shape:', X.shape)

# Standardization
X_mean = X.mean()
X_std = X.std()
Z = (X - X_mean) / X_std

# Covariance Matrix
c = Z.cov()

# Plot covariance matrix
sns.heatmap(c)
plt.title("Covariance Matrix Heatmap")
plt.tight_layout()
plt.show()

# Eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(c)
print('Eigen values:\n', eigenvalues)
print('Eigen values Shape:', eigenvalues.shape)
print('Eigen vectors Shape:', eigenvectors.shape)

# Sort eigenvalues descending
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# Explained variance
explained_var = np.cumsum(eigenvalues) / np.sum(eigenvalues)
print('\nCumulative Explained Variance:\n', explained_var)

# Number of components needed for >= 50% variance
n_components = np.argmax(explained_var >= 0.50) + 1
print(f'\nComponents needed for 50% variance: {n_components}')

# Scree Plot
plt.plot(range(1, len(explained_var) + 1), explained_var, marker='o')
plt.title("Scree Plot")
plt.xlabel("Principal Component")
plt.ylabel("Cumulative Variance Explained")
plt.axhline(y=0.5, color='r', linestyle='--', label='50% threshold')
plt.legend()
plt.tight_layout()
plt.show()
