import pandas as pd

df = pd.read_csv("lab4_dataset2.csv")


# removing empty cell rows
df.dropna(inplace = True)

# removing duplicates
df.drop_duplicates(inplace = True)  
print(df)
df.to_csv('renamed_to_lab5_task3.csv', index=False)