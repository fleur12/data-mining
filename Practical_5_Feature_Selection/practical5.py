# PRACTICAL 5: Feature Selection

import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.feature_selection import SelectKBest, chi2, f_classif, VarianceThreshold, RFE
from sklearn.linear_model import LogisticRegression, LassoCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from mlxtend.feature_selection import SequentialFeatureSelector

# Load Wine dataset
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = pd.Series(wine.target)

print("Sample DataFrame:")
print(X.head())

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# ============================
# 1. FILTER METHODS
# ============================
print("\n=== Filter Methods ===")

# Information Gain (ANOVA F-value)
f_scores, _ = f_classif(X_scaled, y)
info_gain = pd.Series(f_scores, index=X.columns)
print("Top features by Information Gain:")
print(info_gain.sort_values(ascending=False).head())

# Chi-square test
chi_scores, _ = chi2(np.abs(X_scaled), y)
chi2_scores = pd.Series(chi_scores, index=X.columns)
print("\nTop features by Chi-square test:")
print(chi2_scores.sort_values(ascending=False).head())

# Correlation Coefficient
correlations = X.corrwith(y)
print("\nTop features by Correlation Coefficient:")
print(correlations.abs().sort_values(ascending=False).head())

# Variance Threshold
vt = VarianceThreshold(threshold=0.01)
vt.fit(X)
var_features = X.columns[vt.get_support()]
print("\nFeatures selected by Variance Threshold:")
print(var_features.tolist())

# Mean Absolute Difference (MAD)
mad_scores = X.apply(lambda col: np.mean(np.abs(col - np.mean(col))))
print("\nTop features by Mean Absolute Difference (MAD):")
print(mad_scores.sort_values(ascending=False).head())

# ============================
# 2. WRAPPER METHODS
# ============================
print("\n=== Wrapper Methods ===")

lr = LogisticRegression(max_iter=10000)

# Forward Selection
sfs = SequentialFeatureSelector(lr, k_features=5, forward=True)
sfs.fit(X_scaled, y)
print("Forward Selected features:", sfs.k_feature_names_)

# Backward Elimination
sfs_back = SequentialFeatureSelector(lr, k_features=5, forward=False)
sfs_back.fit(X_scaled, y)
print("Backward Selected features:", sfs_back.k_feature_names_)

# Recursive Feature Elimination (RFE)
rfe = RFE(lr, n_features_to_select=5)
rfe.fit(X_scaled, y)
print("RFE selected:", list(X.columns[rfe.support_]))

# ============================
# 3. EMBEDDED METHODS
# ============================
print("\n=== Embedded Methods ===")

# Lasso Regularization
lasso = LassoCV(cv=5, random_state=0).fit(X_scaled, y)
lasso_features = X.columns[lasso.coef_ != 0]
print("Lasso selected features:", lasso_features.tolist())

# Random Forest (Tree-based importance)
rf = RandomForestClassifier(random_state=0)
rf.fit(X_scaled, y)
importances = pd.Series(rf.feature_importances_, index=X.columns)
print("\nTop features by Random Forest Importance:")
print(importances.sort_values(ascending=False).head())
