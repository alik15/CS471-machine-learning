import numpy as np
import pandas as pd

#task 1 

df = pd.read_csv('ML_Lab6_Dataset.csv', index_col=0)
relevant_features = ["LotArea", "GarageArea", "TotalBsmtSF", "BsmtUnfSF", "BsmtFinSF1"]

Xtrain = df[relevant_features].values  # Convert to NumPy array
ytrain = df["SalePrice"].values      # Convert to NumPy array

temp = df[relevant_features].values


# Choose a specific index you want to examine
index_to_check = 0  # Change this to the desired index

for column_index in range(5):
    array = Xtrain[:, column_index]
    max_value = np.max(array)
    min_value = np.min(array)
    denom = max_value - min_value

    value_to_check = Xtrain[index_to_check, column_index]

    # Calculate the normalized value for the specific index
    num = max_value - value_to_check
    normalized_value = num / denom
    
    # Assign the normalized value back to the array
    Xtrain[index_to_check, column_index] = normalized_value

    print(f"Column {column_index} - Max Value: {max_value}, Min Value: {min_value}")
    print(f"Value at index {index_to_check}: {value_to_check}")
    print(f"Normalized Value: {normalized_value}")
    print()

    
    

















