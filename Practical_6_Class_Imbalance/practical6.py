# PRACTICAL 6: Class Imbalance Handling

from sklearn.utils import resample
from sklearn.datasets import make_classification
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

# Create imbalanced dataset (80% class 0, 20% class 1)
X, y = make_classification(
    n_classes=2,
    weights=[0.8, 0.2],
    n_features=4,
    n_samples=100,
    random_state=42
)

df = pd.DataFrame(X, columns=['feature_1', 'feature_2', 'feature_3', 'feature_4'])
df['balance'] = y

print("Original class distribution:")
print(df['balance'].value_counts())

# Separate majority and minority classes
df_major = df[df.balance == 0]
df_minor = df[df.balance == 1]

# Manual Upsampling using sklearn resample
df_minor_sample = resample(
    df_minor,
    replace=True,
    n_samples=80,
    random_state=42
)

df_sample = pd.concat([df_major, df_minor_sample])
print("\nAfter Manual Upsampling (resample):")
print(df_sample['balance'].value_counts())

# Using imblearn RandomOverSampler
Overs = RandomOverSampler(random_state=42)
X_over, y_over = Overs.fit_resample(X, y)

print('\nAfter imblearn RandomOverSampler:')
print('Class 0:', sum(y_over == 0))
print('Class 1:', sum(y_over == 1))
