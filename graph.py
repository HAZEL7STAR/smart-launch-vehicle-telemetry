import pandas as pd

data = pd.read_csv("telemetry.csv")

print(data.head())

print()

print(data.tail())

print()

print(data.shape)

print()

print(data.columns)

print()

print(data.info())