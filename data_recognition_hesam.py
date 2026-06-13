import pandas as pd
import numpy as np

#loaing the data set
df = pd.read_csv('group_26_train.csv')

# basic info :

print("Dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())




# Question 1 : (What columns or features does the data include?)

# List all column names (features)
print("List of all features:")
print(df.columns.tolist())

# Or more detailed with data types
print("\nDetailed feature information:")
print(df.dtypes)

# Or for a clean table view
feature_info = pd.DataFrame({
    'feature_name': df.columns,
    'data_type': df.dtypes.values,
    'null_count': df.isnull().sum().values
})
print(feature_info["null_count"].desc())

