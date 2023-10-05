import pandas as pd


df = pd.read_csv("lab4_dataset1.csv")

print(df.head())
print(df.tail())

print(df.tail(3))
print(df.tail(5))



#part d
print(df.mean())

print(df.mode())
print(df.median())