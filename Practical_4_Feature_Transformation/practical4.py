# PRACTICAL 4: Feature Transformation

import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

# Step 1: Create sample data
data = np.array([1, 2, 3, 4, 5, 6], dtype=float)

# Logarithmic transformation (log1p avoids log(0))
transformer = FunctionTransformer(func=np.log1p)
log_transformed_data = transformer.fit_transform(data)

# Square transformation
square_transformed_data = np.square(data)

# Reciprocal transformation
reciprocal_transformed_data = np.reciprocal(data)

# Trigonometric transformations
sin_transformed_data = np.sin(data)
cos_transformed_data = np.cos(data)
tan_transformed_data = np.tan(data)

# Square root transformation
sqrt_transformed_data = np.sqrt(data)

# Combine all into a DataFrame
results = pd.DataFrame({
   'Original': data,
   'Log (log1p)': log_transformed_data,
   'Square': square_transformed_data,
   'Reciprocal': reciprocal_transformed_data,
   'Sin': sin_transformed_data,
   'Cos': cos_transformed_data,
   'Tan': tan_transformed_data,
   'Square Root': sqrt_transformed_data
})

print(results.to_string(index=False))
